"""
Falcon Signal Pro AI V2.0
EMA Analyzer
"""

import pandas as pd


class EMAAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty:
            return "NO DATA"

        close = data["Close"]

        # yfinance MultiIndex support
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        ema20 = close.ewm(span=20).mean()
        ema50 = close.ewm(span=50).mean()

        last20 = float(ema20.iloc[-1])
        last50 = float(ema50.iloc[-1])

        if last20 > last50:
            return "BULLISH"

        elif last20 < last50:
            return "BEARISH"

        return "SIDEWAYS"
