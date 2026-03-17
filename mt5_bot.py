"""
MT5 Bot — Versión Mejorada
Incluye: logging, gestión de riesgo, trailing stop y estrategia EMA+RSI
Requisitos: pip install MetaTrader5 pandas numpy
"""

import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import logging
import time
from datetime import datetime
from pathlib import Path

# ============================================================
# 0. LOGGING
# ============================================================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / f"bot_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("MT5Bot")

# ============================================================
# 1. CONEXIÓN
# ============================================================

def conectar(cuenta=None, password=None, servidor=None) -> bool:
    """Inicializa y conecta a MT5. Sin parámetros usa la cuenta activa."""
    if not mt5.initialize():
        log.error(f"Error al inicializar MT5: {mt5.last_error()}")
        return False

    if cuenta and password and servidor:
        if not mt5.login(cuenta, password=password, server=servidor):
            log.error(f"Error de login: {mt5.last_error()}")
            return False

    info = mt5.account_info()
    log.info(f"Conectado: {info.name} | Balance: ${info.balance:.2f} | Servidor: {info.server}")
    return True


def desconectar():
    mt5.shutdown()
    log.info("Desconectado de MT5.")


# ============================================================
# 2. INFORMACIÓN DEL MERCADO
# ============================================================

def obtener_precio(simbolo: str) -> dict | None:
    tick = mt5.symbol_info_tick(simbolo)
    if tick is None:
        log.warning(f"Símbolo '{simbolo}' no encontrado.")
        return None
    return {"bid": tick.bid, "ask": tick.ask, "spread": round(tick.ask - tick.bid, 5)}


def obtener_velas(simbolo: str, temporalidad=mt5.TIMEFRAME_H1, cantidad: int = 200) -> pd.DataFrame | None:
    velas = mt5.copy_rates_from_pos(simbolo, temporalidad, 0, cantidad)
    if velas is None or len(velas) == 0:
        log.warning(f"No se pudieron obtener velas para {simbolo}")
        return None
    df = pd.DataFrame(velas)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return df[["time", "open", "high", "low", "close", "tick_volume"]]


# ============================================================
# 3. INDICADORES TÉCNICOS
# ============================================================

def calcular_ema(serie: pd.Series, periodo: int) -> pd.Series:
    return serie.ewm(span=periodo, adjust=False).mean()


def calcular_rsi(serie: pd.Series, periodo: int = 14) -> pd.Series:
    delta = serie.diff()
    ganancia = delta.clip(lower=0).rolling(periodo).mean()
    perdida  = (-delta.clip(upper=0)).rolling(periodo).mean()
    rs = ganancia / perdida.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def calcular_macd(serie: pd.Series, rapido=12, lento=26, senal=9) -> tuple[pd.Series, pd.Series]:
    ema_r = calcular_ema(serie, rapido)
    ema_l = calcular_ema(serie, lento)
    macd  = ema_r - ema_l
    signal = calcular_ema(macd, senal)
    return macd, signal


def generar_senal(df: pd.DataFrame) -> str | None:
    """
    Estrategia: EMA 20/50 cruce + RSI filtro
    - BUY  si EMA20 cruza arriba de EMA50 Y RSI entre 45-65
    - SELL si EMA20 cruza abajo de EMA50 Y RSI entre 35-55
    Retorna 'buy', 'sell' o None.
    """
    df = df.copy()
    df["ema20"] = calcular_ema(df["close"], 20)
    df["ema50"] = calcular_ema(df["close"], 50)
    df["rsi"]   = calcular_rsi(df["close"], 14)

    ema20_prev = df["ema20"].iloc[-2]
    ema50_prev = df["ema50"].iloc[-2]
    ema20_curr = df["ema20"].iloc[-1]
    ema50_curr = df["ema50"].iloc[-1]
    rsi        = df["rsi"].iloc[-1]

    cruce_alcista = ema20_prev < ema50_prev and ema20_curr > ema50_curr
    cruce_bajista = ema20_prev > ema50_prev and ema20_curr < ema50_curr

    if cruce_alcista and 45 <= rsi <= 65:
        log.info(f"Señal BUY  | EMA20={ema20_curr:.5f} EMA50={ema50_curr:.5f} RSI={rsi:.1f}")
        return "buy"
    if cruce_bajista and 35 <= rsi <= 55:
        log.info(f"Señal SELL | EMA20={ema20_curr:.5f} EMA50={ema50_curr:.5f} RSI={rsi:.1f}")
        return "sell"
    return None


# ============================================================
# 4. GESTIÓN DE RIESGO
# ============================================================

def calcular_lotes(simbolo: str, sl_points: int, riesgo_pct: float = 1.0) -> float:
    """
    Calcula el tamaño de lote para no arriesgar más del riesgo_pct% del balance.

    Fórmula: lotes = (balance * riesgo_pct/100) / (sl_points * valor_por_punto)
    """
    cuenta  = mt5.account_info()
    info    = mt5.symbol_info(simbolo)
    if cuenta is None or info is None or sl_points == 0:
        return info.volume_min if info else 0.01

    balance = cuenta.balance
    riesgo  = balance * (riesgo_pct / 100)

    # Valor de un punto por lote en la divisa de la cuenta
    tick_value  = info.trade_tick_value
    tick_size   = info.trade_tick_size
    valor_punto = tick_value / tick_size * info.point

    if valor_punto == 0:
        return info.volume_min

    lotes_raw = riesgo / (sl_points * valor_punto)
    # Redondear al step y limitar min/max
    step  = info.volume_step
    lotes = round(lotes_raw / step) * step
    lotes = max(info.volume_min, min(lotes, info.volume_max))

    log.info(f"Riesgo {riesgo_pct}% de ${balance:.2f} → {lotes} lotes (SL={sl_points}pts)")
    return lotes


# ============================================================
# 5. EJECUTAR OPERACIONES
# ============================================================

def abrir_orden(
    simbolo: str,
    tipo: str,
    lotes: float,
    sl_points: int = 0,
    tp_points: int = 0,
    comentario: str = "PythonBot",
) -> object | None:
    """Abre una orden de mercado. tipo: 'buy' o 'sell'"""
    info = mt5.symbol_info(simbolo)
    if info is None:
        log.error(f"Símbolo '{simbolo}' no disponible.")
        return None
    if not info.visible:
        mt5.symbol_select(simbolo, True)

    tick  = mt5.symbol_info_tick(simbolo)
    point = info.point

    if tipo == "buy":
        order_type = mt5.ORDER_TYPE_BUY
        precio = tick.ask
        sl = precio - sl_points * point if sl_points else 0.0
        tp = precio + tp_points * point if tp_points else 0.0
    elif tipo == "sell":
        order_type = mt5.ORDER_TYPE_SELL
        precio = tick.bid
        sl = precio + sl_points * point if sl_points else 0.0
        tp = precio - tp_points * point if tp_points else 0.0
    else:
        log.error("Tipo debe ser 'buy' o 'sell'")
        return None

    request = {
        "action":       mt5.TRADE_ACTION_DEAL,
        "symbol":       simbolo,
        "volume":       lotes,
        "type":         order_type,
        "price":        precio,
        "sl":           sl,
        "tp":           tp,
        "deviation":    20,
        "magic":        123456,
        "comment":      comentario,
        "type_time":    mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    resultado = mt5.order_send(request)
    if resultado.retcode != mt5.TRADE_RETCODE_DONE:
        log.error(f"Error al enviar orden: {resultado.retcode} - {resultado.comment}")
        return None

    log.info(f"Orden ejecutada: {tipo.upper()} {lotes} {simbolo} @ {precio} | SL:{sl:.5f} TP:{tp:.5f}")
    return resultado


# ============================================================
# 6. TRAILING STOP
# ============================================================

def aplicar_trailing_stop(simbolo: str, trail_points: int, magic: int = 123456):
    """
    Ajusta el SL de todas las posiciones abiertas del símbolo
    cuando el precio se mueve a favor trail_points puntos.
    Llama a esta función en cada ciclo del loop principal.
    """
    posiciones = mt5.positions_get(symbol=simbolo)
    if not posiciones:
        return

    info  = mt5.symbol_info(simbolo)
    point = info.point
    tick  = mt5.symbol_info_tick(simbolo)

    for pos in posiciones:
        if pos.magic != magic:
            continue

        if pos.type == mt5.ORDER_TYPE_BUY:
            nuevo_sl = tick.bid - trail_points * point
            # Solo subir el SL, nunca bajarlo
            if nuevo_sl > pos.sl + point:
                _modificar_sl(pos, nuevo_sl)

        elif pos.type == mt5.ORDER_TYPE_SELL:
            nuevo_sl = tick.ask + trail_points * point
            # Solo bajar el SL, nunca subirlo
            if nuevo_sl < pos.sl - point or pos.sl == 0:
                _modificar_sl(pos, nuevo_sl)


def _modificar_sl(pos, nuevo_sl: float):
    request = {
        "action":   mt5.TRADE_ACTION_SLTP,
        "position": pos.ticket,
        "sl":       nuevo_sl,
        "tp":       pos.tp,
    }
    res = mt5.order_send(request)
    if res.retcode == mt5.TRADE_RETCODE_DONE:
        log.info(f"Trailing SL actualizado | Ticket:{pos.ticket} SL:{nuevo_sl:.5f}")
    else:
        log.warning(f"Error actualizando SL: {res.retcode} - {res.comment}")


# ============================================================
# 7. GESTIÓN DE POSICIONES
# ============================================================

def posiciones_abiertas(simbolo: str = None) -> pd.DataFrame | None:
    pos = mt5.positions_get(symbol=simbolo) if simbolo else mt5.positions_get()
    if not pos:
        log.info("No hay posiciones abiertas.")
        return None
    df = pd.DataFrame(list(pos), columns=pos[0]._asdict().keys())
    df["type"] = df["type"].map({0: "BUY", 1: "SELL"})
    return df[["ticket", "symbol", "type", "volume", "price_open", "sl", "tp", "profit"]]


def cerrar_posicion(ticket: int) -> object | None:
    pos = mt5.positions_get(ticket=ticket)
    if not pos:
        log.warning(f"Posición {ticket} no encontrada.")
        return None

    pos = pos[0]
    tipo_cierre = mt5.ORDER_TYPE_SELL if pos.type == 0 else mt5.ORDER_TYPE_BUY
    precio = (
        mt5.symbol_info_tick(pos.symbol).bid if pos.type == 0
        else mt5.symbol_info_tick(pos.symbol).ask
    )

    request = {
        "action":       mt5.TRADE_ACTION_DEAL,
        "symbol":       pos.symbol,
        "volume":       pos.volume,
        "type":         tipo_cierre,
        "position":     ticket,
        "price":        precio,
        "deviation":    20,
        "magic":        123456,
        "comment":      "Cierre PythonBot",
        "type_time":    mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    resultado = mt5.order_send(request)
    if resultado.retcode != mt5.TRADE_RETCODE_DONE:
        log.error(f"Error al cerrar {ticket}: {resultado.retcode} - {resultado.comment}")
        return None

    log.info(f"Posición {ticket} cerrada @ {precio:.5f} | Profit: {pos.profit:.2f}")
    return resultado


def cerrar_todas(simbolo: str = None):
    pos = mt5.positions_get(symbol=simbolo) if simbolo else mt5.positions_get()
    if not pos:
        log.info("No hay posiciones para cerrar.")
        return
    for p in pos:
        cerrar_posicion(p.ticket)


# ============================================================
# 8. HISTORIAL
# ============================================================

def historial_ordenes(dias: int = 7) -> pd.DataFrame | None:
    desde = datetime.now() - pd.Timedelta(days=dias)
    deals = mt5.history_deals_get(desde, datetime.now())
    if not deals:
        log.info("Sin historial.")
        return None
    df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return df[["time", "symbol", "type", "volume", "price", "profit", "comment"]]


# ============================================================
# 9. LOOP PRINCIPAL (ejemplo de uso)
# ============================================================

SIMBOLO       = "EURUSD"
TEMPORALIDAD  = mt5.TIMEFRAME_H1
SL_POINTS     = 300
TP_POINTS     = 600
TRAIL_POINTS  = 150        # puntos de trailing stop
RIESGO_PCT    = 1.0        # % del balance a arriesgar por operación
INTERVALO_SEG = 60         # segundos entre cada ciclo


def loop_principal():
    """Loop que revisa señales y aplica trailing stop en cada ciclo."""
    log.info("=== Bot iniciado ===")

    while True:
        try:
            df = obtener_velas(SIMBOLO, TEMPORALIDAD, 200)
            if df is None:
                time.sleep(INTERVALO_SEG)
                continue

            # Trailing stop en posiciones existentes
            aplicar_trailing_stop(SIMBOLO, TRAIL_POINTS)

            # Solo abrir nueva posición si no hay ninguna abierta
            posiciones = mt5.positions_get(symbol=SIMBOLO)
            if posiciones:
                log.info(f"Posición activa en {SIMBOLO}, esperando...")
                time.sleep(INTERVALO_SEG)
                continue

            senal = generar_senal(df)
            if senal:
                lotes = calcular_lotes(SIMBOLO, SL_POINTS, RIESGO_PCT)
                abrir_orden(SIMBOLO, senal, lotes, SL_POINTS, TP_POINTS)

        except KeyboardInterrupt:
            log.info("Bot detenido por el usuario.")
            break
        except Exception as e:
            log.error(f"Error en loop: {e}", exc_info=True)

        time.sleep(INTERVALO_SEG)


# ============================================================
# ENTRADA
# ============================================================

if __name__ == "__main__":
    if conectar():
        try:
            loop_principal()
        finally:
            cerrar_todas()
            desconectar()
