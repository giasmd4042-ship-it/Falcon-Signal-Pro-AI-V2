"""
Falcon Signal Pro AI V2.0
MACD Analyzer
"""

import pandas as pd


class MACDAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty:
            return "NO DATA"

        close = data["Close"]

        # yfinance MultiIndex support
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()

        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()

        last_macd = float(macd.iloc[-1])
        last_signal = float(signal.iloc[-1])

        if last_macd > last_signal:
            return "BULLISH"

        elif last_macd < last_signal:
            return "BEARISH"

        return "SIDEWAYS"
