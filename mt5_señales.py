"""
MT5 Señales en Vivo — Consulta el socket de MT5 y da recomendaciones de trading
Corre esto en tu PC mientras MT5 está abierto.
Requisitos: pip install MetaTrader5 pandas numpy colorama
"""

import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime

# ── Colores en consola (opcional, pip install colorama) ──────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    VERDE   = Fore.GREEN
    ROJO    = Fore.RED
    AMARILLO = Fore.YELLOW
    CYAN    = Fore.CYAN
    BLANCO  = Fore.WHITE
    RESET   = Style.RESET_ALL
    NEGRITA = Style.BRIGHT
except ImportError:
    VERDE = ROJO = AMARILLO = CYAN = BLANCO = RESET = NEGRITA = ""

# ============================================================
# CONFIGURACIÓN
# ============================================================

SIMBOLOS       = ["GBPJPY", "EURUSD", "XAUUSD"]   # pares a monitorear
INTERVALO_SEG  = 15                                 # segundos entre análisis
TEMPORALIDAD   = mt5.TIMEFRAME_M5                  # velas de 5 minutos
VELAS          = 100                                # velas a analizar

# ============================================================
# INDICADORES
# ============================================================

def ema(serie, n):
    return serie.ewm(span=n, adjust=False).mean()

def rsi(serie, n=14):
    d = serie.diff()
    g = d.clip(lower=0).rolling(n).mean()
    p = (-d.clip(upper=0)).rolling(n).mean()
    return 100 - 100 / (1 + g / p.replace(0, np.nan))

def atr(df, n=14):
    h, l, c = df["high"], df["low"], df["close"].shift(1)
    tr = pd.concat([h - l, (h - c).abs(), (l - c).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def bollinger(serie, n=20, k=2):
    media = serie.rolling(n).mean()
    std   = serie.rolling(n).std()
    return media + k * std, media, media - k * std

# ============================================================
# ANÁLISIS PRINCIPAL
# ============================================================

def analizar(simbolo: str) -> dict:
    """Descarga velas y calcula señal de trading."""
    velas = mt5.copy_rates_from_pos(simbolo, TEMPORALIDAD, 0, VELAS)
    if velas is None or len(velas) < 50:
        return {"error": "Sin datos"}

    df = pd.DataFrame(velas)
    df["time"] = pd.to_datetime(df["time"], unit="s")

    # Indicadores
    df["ema9"]  = ema(df["close"], 9)
    df["ema21"] = ema(df["close"], 21)
    df["ema50"] = ema(df["close"], 50)
    df["rsi"]   = rsi(df["close"], 14)
    df["atr"]   = atr(df, 14)
    df["bb_up"], df["bb_mid"], df["bb_dn"] = bollinger(df["close"])

    c  = df.iloc[-1]   # vela actual
    p  = df.iloc[-2]   # vela anterior

    tick  = mt5.symbol_info_tick(simbolo)
    info  = mt5.symbol_info(simbolo)
    price = tick.ask if tick else 0

    # ── Puntuación de señal ──────────────────────────────────
    score_buy  = 0
    score_sell = 0
    razones_buy  = []
    razones_sell = []

    # EMA 9 > 21 (tendencia corta)
    if c["ema9"] > c["ema21"]:
        score_buy += 2
        razones_buy.append("EMA9 > EMA21 (tendencia alcista)")
    else:
        score_sell += 2
        razones_sell.append("EMA9 < EMA21 (tendencia bajista)")

    # EMA 21 > 50 (tendencia media)
    if c["ema21"] > c["ema50"]:
        score_buy += 2
        razones_buy.append("EMA21 > EMA50 (momentum alcista)")
    else:
        score_sell += 2
        razones_sell.append("EMA21 < EMA50 (momentum bajista)")

    # RSI
    r = c["rsi"]
    if 50 < r < 70:
        score_buy += 2
        razones_buy.append(f"RSI={r:.0f} zona alcista")
    elif 30 < r < 50:
        score_sell += 2
        razones_sell.append(f"RSI={r:.0f} zona bajista")
    elif r >= 70:
        score_sell += 1
        razones_sell.append(f"RSI={r:.0f} sobrecomprado ⚠")
    elif r <= 30:
        score_buy += 1
        razones_buy.append(f"RSI={r:.0f} sobrevendido ⚠")

    # Precio vs Bollinger
    if price <= c["bb_dn"]:
        score_buy += 2
        razones_buy.append("Precio en banda baja Bollinger (rebote posible)")
    elif price >= c["bb_up"]:
        score_sell += 2
        razones_sell.append("Precio en banda alta Bollinger (rechazo posible)")

    # Cruce reciente EMA9/EMA21
    cruce_up   = p["ema9"] < p["ema21"] and c["ema9"] > c["ema21"]
    cruce_down = p["ema9"] > p["ema21"] and c["ema9"] < c["ema21"]
    if cruce_up:
        score_buy += 3
        razones_buy.append("*** CRUCE ALCISTA EMA9/EMA21 (señal fuerte)")
    if cruce_down:
        score_sell += 3
        razones_sell.append("*** CRUCE BAJISTA EMA9/EMA21 (señal fuerte)")

    # ── Decisión final ───────────────────────────────────────
    atr_val = c["atr"]
    sl_buy  = round(price - atr_val * 1.5, info.digits)
    tp_buy  = round(price + atr_val * 3.0, info.digits)
    sl_sell = round(price + atr_val * 1.5, info.digits)
    tp_sell = round(price - atr_val * 3.0, info.digits)

    total = score_buy + score_sell
    if total == 0:
        total = 1

    fuerza_buy  = int((score_buy  / total) * 100)
    fuerza_sell = int((score_sell / total) * 100)

    if score_buy > score_sell and score_buy >= 5:
        accion = "BUY"
        confianza = fuerza_buy
        razones = razones_buy
        sl, tp = sl_buy, tp_buy
    elif score_sell > score_buy and score_sell >= 5:
        accion = "SELL"
        confianza = fuerza_sell
        razones = razones_sell
        sl, tp = sl_sell, tp_sell
    else:
        accion = "ESPERAR"
        confianza = 0
        razones = ["Señales mixtas, sin dirección clara"]
        sl = tp = 0

    return {
        "simbolo":    simbolo,
        "precio":     price,
        "bid":        tick.bid if tick else 0,
        "ask":        tick.ask if tick else 0,
        "spread":     round((tick.ask - tick.bid) / info.point) if tick and info else 0,
        "accion":     accion,
        "confianza":  confianza,
        "sl":         sl,
        "tp":         tp,
        "atr":        round(atr_val, info.digits) if info else 0,
        "rsi":        round(r, 1),
        "razones":    razones,
        "hora":       datetime.now().strftime("%H:%M:%S"),
    }

# ============================================================
# MOSTRAR RESULTADO EN CONSOLA
# ============================================================

def imprimir_senal(s: dict):
    if "error" in s:
        print(f"{ROJO}{s['simbolo']}: {s['error']}{RESET}")
        return

    color = VERDE if s["accion"] == "BUY" else ROJO if s["accion"] == "SELL" else AMARILLO
    barra = "█" * (s["confianza"] // 10) + "░" * (10 - s["confianza"] // 10)

    print(f"\n{NEGRITA}{CYAN}{'─'*52}{RESET}")
    print(f"{NEGRITA}{s['simbolo']}{RESET}  {BLANCO}{s['hora']}{RESET}")
    print(f"  Precio: {NEGRITA}{s['precio']}{RESET}  "
          f"BID {s['bid']}  ASK {s['ask']}  Spread: {s['spread']} pts")
    print(f"  RSI: {s['rsi']:.0f}   ATR: {s['atr']}")
    print(f"\n  Señal:  {color}{NEGRITA}{s['accion']}{RESET}  [{barra}] {s['confianza']}%")

    if s["accion"] != "ESPERAR":
        print(f"  SL:     {ROJO}{s['sl']}{RESET}")
        print(f"  TP:     {VERDE}{s['tp']}{RESET}")
        rr = round(abs(s["tp"] - s["precio"]) / abs(s["sl"] - s["precio"]), 1) if s["sl"] else 0
        print(f"  R/R:    1:{rr}")

    print(f"\n  Motivos:")
    for r in s["razones"]:
        print(f"    • {r}")

# ============================================================
# LOOP PRINCIPAL
# ============================================================

def main():
    print(f"\n{NEGRITA}{CYAN}  MT5 SEÑALES EN VIVO{RESET}")
    print(f"  Pares: {', '.join(SIMBOLOS)}")
    print(f"  Temporalidad: M5  |  Intervalo: {INTERVALO_SEG}s")
    print(f"  Presiona Ctrl+C para detener\n")

    if not mt5.initialize():
        print(f"{ROJO}Error: MT5 no está abierto en esta PC.{RESET}")
        print("Abre MetaTrader 5 primero y vuelve a ejecutar este script.")
        return

    info = mt5.account_info()
    if info:
        print(f"{VERDE}Conectado: {info.name}  Balance: ${info.balance:.2f}{RESET}\n")

    try:
        ciclo = 0
        while True:
            ciclo += 1
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{NEGRITA}{CYAN}══ MT5 SEÑALES EN VIVO ══  ciclo #{ciclo}  "
                  f"{datetime.now().strftime('%H:%M:%S')}{RESET}")
            if info:
                print(f"Balance: ${info.balance:.2f}  |  Equity: ${mt5.account_info().equity:.2f}\n")

            for simbolo in SIMBOLOS:
                senal = analizar(simbolo)
                imprimir_senal(senal)

            print(f"\n{AMARILLO}Próximo análisis en {INTERVALO_SEG}s...{RESET}")
            time.sleep(INTERVALO_SEG)

    except KeyboardInterrupt:
        print(f"\n{AMARILLO}Detenido.{RESET}")
    finally:
        mt5.shutdown()


if __name__ == "__main__":
    main()
