"""
MT5 AutoBot — Entrada y salida automática en tiempo real
Requisitos: pip install MetaTrader5 pandas numpy colorama
IMPORTANTE: Prueba en cuenta DEMO antes de usar dinero real.
"""

import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
import os
import logging
from datetime import datetime
from pathlib import Path

# ── Colores ──────────────────────────────────────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    V=Fore.GREEN; R=Fore.RED; Y=Fore.YELLOW; C=Fore.CYAN; W=Fore.WHITE
    RESET=Style.RESET_ALL; B=Style.BRIGHT
except ImportError:
    V=R=Y=C=W=RESET=B=""

# ── Logging ──────────────────────────────────────────────────────────────────
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"logs/autobot_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("AutoBot")

# ╔══════════════════════════════════════════════════════╗
# ║               CONFIGURACIÓN                          ║
# ╚══════════════════════════════════════════════════════╝

SIMBOLOS        = ["GBPJPY", "EURUSD", "XAUUSD"]
TEMPORALIDAD    = mt5.TIMEFRAME_M5   # velas M5 para señales
INTERVALO_SEG   = 10                 # segundos entre ciclos
MAGIC           = 888999             # ID único del bot

# Riesgo
RIESGO_PCT      = 1.0    # % del balance por operación (1% = conservador)
MAX_POSICIONES  = 2      # máximo de posiciones abiertas al mismo tiempo
PERDIDA_DIA_PCT = 5.0    # detener bot si pierde este % del balance en el día

# Trailing stop
TRAIL_ATR_MULT  = 1.0    # mover SL cuando el precio avanza 1x ATR

# Señal mínima para entrar
CONFIANZA_MIN   = 60     # % mínimo de confianza para abrir orden

# ╔══════════════════════════════════════════════════════╗
# ║               ESTADO GLOBAL                          ║
# ╚══════════════════════════════════════════════════════╝

balance_inicio_dia = None
bot_activo         = True

# ╔══════════════════════════════════════════════════════╗
# ║               INDICADORES                            ║
# ╚══════════════════════════════════════════════════════╝

def ema(s, n): return s.ewm(span=n, adjust=False).mean()

def rsi(s, n=14):
    d = s.diff()
    g = d.clip(lower=0).rolling(n).mean()
    p = (-d.clip(upper=0)).rolling(n).mean()
    return 100 - 100 / (1 + g / p.replace(0, np.nan))

def atr(df, n=14):
    h, l, c = df["high"], df["low"], df["close"].shift(1)
    tr = pd.concat([h-l, (h-c).abs(), (l-c).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def bollinger(s, n=20, k=2):
    m = s.rolling(n).mean(); std = s.rolling(n).std()
    return m + k*std, m, m - k*std

# ╔══════════════════════════════════════════════════════╗
# ║               SEÑAL                                  ║
# ╚══════════════════════════════════════════════════════╝

def analizar(simbolo: str) -> dict | None:
    velas = mt5.copy_rates_from_pos(simbolo, TEMPORALIDAD, 0, 100)
    if velas is None or len(velas) < 52:
        return None

    df = pd.DataFrame(velas)
    df["ema9"]  = ema(df["close"], 9)
    df["ema21"] = ema(df["close"], 21)
    df["ema50"] = ema(df["close"], 50)
    df["rsi"]   = rsi(df["close"], 14)
    df["atr"]   = atr(df, 14)
    df["bb_up"], _, df["bb_dn"] = bollinger(df["close"])

    c, p   = df.iloc[-1], df.iloc[-2]
    tick   = mt5.symbol_info_tick(simbolo)
    info   = mt5.symbol_info(simbolo)
    if not tick or not info:
        return None

    sb, ss = 0, 0
    rb, rs = [], []

    if c["ema9"]  > c["ema21"]: sb += 2; rb.append("EMA9>EMA21 alcista")
    else:                        ss += 2; rs.append("EMA9<EMA21 bajista")

    if c["ema21"] > c["ema50"]: sb += 2; rb.append("EMA21>EMA50 momentum +")
    else:                        ss += 2; rs.append("EMA21<EMA50 momentum -")

    r = c["rsi"]
    if   50 < r < 70: sb += 2; rb.append(f"RSI {r:.0f} zona alcista")
    elif 30 < r < 50: ss += 2; rs.append(f"RSI {r:.0f} zona bajista")
    elif r >= 70:     ss += 1; rs.append(f"RSI {r:.0f} sobrecomprado")
    elif r <= 30:     sb += 1; rb.append(f"RSI {r:.0f} sobrevendido")

    price = tick.ask
    if price <= c["bb_dn"]: sb += 2; rb.append("Precio en BB baja")
    elif price >= c["bb_up"]:ss += 2; rs.append("Precio en BB alta")

    if p["ema9"] < p["ema21"] and c["ema9"] > c["ema21"]:
        sb += 3; rb.append("★ CRUCE ALCISTA EMA9/EMA21")
    if p["ema9"] > p["ema21"] and c["ema9"] < c["ema21"]:
        ss += 3; rs.append("★ CRUCE BAJISTA EMA9/EMA21")

    total = max(sb + ss, 1)
    atr_v = c["atr"]

    if sb > ss and int(sb/total*100) >= CONFIANZA_MIN:
        return {"simbolo": simbolo, "accion": "buy",  "confianza": int(sb/total*100),
                "razones": rb, "atr": atr_v, "info": info,
                "sl": round(tick.ask - atr_v*1.5, info.digits),
                "tp": round(tick.ask + atr_v*3.0, info.digits),
                "rsi": r}
    if ss > sb and int(ss/total*100) >= CONFIANZA_MIN:
        return {"simbolo": simbolo, "accion": "sell", "confianza": int(ss/total*100),
                "razones": rs, "atr": atr_v, "info": info,
                "sl": round(tick.bid + atr_v*1.5, info.digits),
                "tp": round(tick.bid - atr_v*3.0, info.digits),
                "rsi": r}
    return None

# ╔══════════════════════════════════════════════════════╗
# ║               RIESGO                                 ║
# ╚══════════════════════════════════════════════════════╝

def calcular_lotes(simbolo: str, sl_pts: float) -> float:
    cuenta = mt5.account_info()
    info   = mt5.symbol_info(simbolo)
    if not cuenta or not info or sl_pts == 0:
        return info.volume_min if info else 0.01

    riesgo      = cuenta.balance * (RIESGO_PCT / 100)
    valor_punto = info.trade_tick_value / info.trade_tick_size * info.point
    if valor_punto == 0:
        return info.volume_min

    lotes = riesgo / (sl_pts * valor_punto)
    lotes = round(lotes / info.volume_step) * info.volume_step
    return max(info.volume_min, min(lotes, info.volume_max))

def perdida_dia_excedida() -> bool:
    global balance_inicio_dia
    cuenta = mt5.account_info()
    if not cuenta or balance_inicio_dia is None:
        return False
    perdida_pct = (balance_inicio_dia - cuenta.equity) / balance_inicio_dia * 100
    return perdida_pct >= PERDIDA_DIA_PCT

# ╔══════════════════════════════════════════════════════╗
# ║               ÓRDENES                                ║
# ╚══════════════════════════════════════════════════════╝

def ya_tiene_posicion(simbolo: str) -> bool:
    pos = mt5.positions_get(symbol=simbolo)
    return bool(pos and any(p.magic == MAGIC for p in pos))

def total_posiciones() -> int:
    pos = mt5.positions_get()
    if not pos:
        return 0
    return sum(1 for p in pos if p.magic == MAGIC)

def abrir(senal: dict) -> bool:
    simbolo = senal["simbolo"]
    tipo    = senal["accion"]
    info    = senal["info"]

    if not info.visible:
        mt5.symbol_select(simbolo, True)

    tick = mt5.symbol_info_tick(simbolo)
    if tipo == "buy":
        precio, order_type = tick.ask, mt5.ORDER_TYPE_BUY
    else:
        precio, order_type = tick.bid, mt5.ORDER_TYPE_SELL

    sl_pts = abs(precio - senal["sl"]) / info.point
    lotes  = calcular_lotes(simbolo, sl_pts)

    req = {
        "action":       mt5.TRADE_ACTION_DEAL,
        "symbol":       simbolo,
        "volume":       lotes,
        "type":         order_type,
        "price":        precio,
        "sl":           senal["sl"],
        "tp":           senal["tp"],
        "deviation":    30,
        "magic":        MAGIC,
        "comment":      f"AutoBot {tipo.upper()} {senal['confianza']}%",
        "type_time":    mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    res = mt5.order_send(req)
    if res.retcode == mt5.TRADE_RETCODE_DONE:
        log.info(f"✔ ABIERTO {tipo.upper()} {lotes} {simbolo} @ {precio} "
                 f"SL:{senal['sl']} TP:{senal['tp']} conf:{senal['confianza']}%")
        return True
    else:
        log.error(f"✘ Error abriendo {simbolo}: {res.retcode} — {res.comment}")
        return False

def cerrar(ticket: int):
    pos = mt5.positions_get(ticket=ticket)
    if not pos:
        return
    pos = pos[0]
    tick  = mt5.symbol_info_tick(pos.symbol)
    tipo  = mt5.ORDER_TYPE_SELL if pos.type == 0 else mt5.ORDER_TYPE_BUY
    precio = tick.bid if pos.type == 0 else tick.ask

    req = {
        "action":       mt5.TRADE_ACTION_DEAL,
        "symbol":       pos.symbol,
        "volume":       pos.volume,
        "type":         tipo,
        "position":     ticket,
        "price":        precio,
        "deviation":    30,
        "magic":        MAGIC,
        "comment":      "AutoBot cierre",
        "type_time":    mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    res = mt5.order_send(req)
    if res.retcode == mt5.TRADE_RETCODE_DONE:
        log.info(f"✔ CERRADO ticket:{ticket} {pos.symbol} @ {precio} profit:{pos.profit:.2f}")
    else:
        log.error(f"✘ Error cerrando {ticket}: {res.retcode} — {res.comment}")

# ╔══════════════════════════════════════════════════════╗
# ║               TRAILING STOP                          ║
# ╚══════════════════════════════════════════════════════╝

def trailing_stop():
    pos = mt5.positions_get()
    if not pos:
        return
    for p in pos:
        if p.magic != MAGIC:
            continue
        info  = mt5.symbol_info(p.symbol)
        tick  = mt5.symbol_info_tick(p.symbol)
        if not info or not tick:
            continue

        atr_v = _ultimo_atr(p.symbol)
        trail = atr_v * TRAIL_ATR_MULT

        if p.type == mt5.ORDER_TYPE_BUY:
            nuevo_sl = round(tick.bid - trail, info.digits)
            if nuevo_sl > p.sl + info.point:
                _modificar_sl(p, nuevo_sl)
        elif p.type == mt5.ORDER_TYPE_SELL:
            nuevo_sl = round(tick.ask + trail, info.digits)
            if p.sl == 0 or nuevo_sl < p.sl - info.point:
                _modificar_sl(p, nuevo_sl)

def _ultimo_atr(simbolo: str) -> float:
    velas = mt5.copy_rates_from_pos(simbolo, TEMPORALIDAD, 0, 20)
    if velas is None:
        return 0
    df = pd.DataFrame(velas)
    h, l, c = df["high"], df["low"], df["close"].shift(1)
    tr = pd.concat([h-l, (h-c).abs(), (l-c).abs()], axis=1).max(axis=1)
    return tr.rolling(14).mean().iloc[-1]

def _modificar_sl(pos, nuevo_sl: float):
    res = mt5.order_send({
        "action":   mt5.TRADE_ACTION_SLTP,
        "position": pos.ticket,
        "sl":       nuevo_sl,
        "tp":       pos.tp,
    })
    if res.retcode == mt5.TRADE_RETCODE_DONE:
        log.info(f"  Trailing SL → {nuevo_sl:.5f}  ticket:{pos.ticket}")

# ╔══════════════════════════════════════════════════════╗
# ║               PANTALLA                               ║
# ╚══════════════════════════════════════════════════════╝

def mostrar_estado(ciclo: int):
    os.system("cls" if os.name == "nt" else "clear")
    cuenta = mt5.account_info()
    hora   = datetime.now().strftime("%H:%M:%S")

    print(f"{B}{C}══════════════════════════════════════════{RESET}")
    print(f"{B}{C}   MT5 AUTOBOT — TIEMPO REAL   ciclo #{ciclo}{RESET}")
    print(f"{B}{C}══════════════════════════════════════════{RESET}")
    if cuenta:
        equity_color = V if cuenta.equity >= cuenta.balance else R
        print(f"  {hora}  |  Balance: {B}${cuenta.balance:.2f}{RESET}  "
              f"Equity: {equity_color}{B}${cuenta.equity:.2f}{RESET}")
        if balance_inicio_dia:
            pnl = cuenta.equity - balance_inicio_dia
            col = V if pnl >= 0 else R
            print(f"  P&L hoy: {col}{B}{'+' if pnl>=0 else ''}{pnl:.2f}{RESET}")
    print()

    # Posiciones abiertas
    pos = mt5.positions_get()
    if pos:
        print(f"  {B}Posiciones abiertas:{RESET}")
        for p in pos:
            if p.magic != MAGIC:
                continue
            tipo_str = f"{V}BUY{RESET}" if p.type == 0 else f"{R}SELL{RESET}"
            pnl_col  = V if p.profit >= 0 else R
            print(f"    {p.symbol} {tipo_str} {p.volume} lots  "
                  f"entrada:{p.price_open}  SL:{p.sl:.5f}  "
                  f"P&L: {pnl_col}{B}{p.profit:+.2f}{RESET}")
    else:
        print(f"  {Y}Sin posiciones abiertas{RESET}")
    print()

# ╔══════════════════════════════════════════════════════╗
# ║               LOOP PRINCIPAL                         ║
# ╚══════════════════════════════════════════════════════╝

def main():
    global balance_inicio_dia, bot_activo

    if not mt5.initialize():
        print(f"{R}MT5 no está abierto. Ábrelo primero.{RESET}")
        return

    cuenta = mt5.account_info()
    if not cuenta:
        print(f"{R}No se pudo obtener info de cuenta.{RESET}")
        return

    balance_inicio_dia = cuenta.balance
    log.info(f"AutoBot iniciado | {cuenta.name} | Balance: ${cuenta.balance:.2f}")

    ciclo = 0
    try:
        while bot_activo:
            ciclo += 1

            # ── Guardia de pérdida diaria ──────────────────
            if perdida_dia_excedida():
                log.warning(f"Pérdida diaria >{PERDIDA_DIA_PCT}% alcanzada. Bot detenido.")
                # Cerrar todo antes de parar
                pos = mt5.positions_get()
                if pos:
                    for p in pos:
                        if p.magic == MAGIC:
                            cerrar(p.ticket)
                break

            mostrar_estado(ciclo)

            # ── Trailing stop en posiciones existentes ─────
            trailing_stop()

            # ── Buscar señales y abrir si hay cupo ─────────
            if total_posiciones() < MAX_POSICIONES:
                for simbolo in SIMBOLOS:
                    if ya_tiene_posicion(simbolo):
                        continue
                    senal = analizar(simbolo)
                    if senal:
                        print(f"  {B}{C}Señal detectada:{RESET} "
                              f"{senal['simbolo']} "
                              f"{'BUY' if senal['accion']=='buy' else 'SELL'} "
                              f"{senal['confianza']}%")
                        for r in senal["razones"]:
                            print(f"    • {r}")
                        print()
                        abrir(senal)
            else:
                print(f"  {Y}Máximo de posiciones alcanzado ({MAX_POSICIONES}){RESET}\n")

            print(f"  {Y}Próximo ciclo en {INTERVALO_SEG}s...{RESET}")
            time.sleep(INTERVALO_SEG)

    except KeyboardInterrupt:
        log.info("Bot detenido por el usuario (Ctrl+C)")
    finally:
        mt5.shutdown()
        log.info("Desconectado de MT5.")


if __name__ == "__main__":
    print(f"""
{B}{Y}╔══════════════════════════════════════════╗
║   MT5 AUTOBOT — ADVERTENCIA IMPORTANTE   ║
╠══════════════════════════════════════════╣
║  Este bot opera con dinero REAL.         ║
║  Prueba en cuenta DEMO primero.          ║
║  El trading conlleva riesgo de pérdida.  ║
╚══════════════════════════════════════════╝{RESET}

  Configuración activa:
    Pares:         {', '.join(SIMBOLOS)}
    Riesgo/op:     {RIESGO_PCT}% del balance
    Max posiciones:{MAX_POSICIONES}
    Stop diario:   -{PERDIDA_DIA_PCT}% del balance
    Confianza min: {CONFIANZA_MIN}%
    Trailing stop: {TRAIL_ATR_MULT}x ATR

""")
    confirmar = input("  ¿Continuar? (escribe SI para confirmar): ").strip()
    if confirmar.upper() == "SI":
        main()
    else:
        print("Cancelado.")
