"""
Falcon Signal Pro AI V2.0
Trend Analyzer
"""

import pandas as pd


class TrendAnalyzer:

    def detect_trend(self, data: pd.DataFrame) -> str:

        if data.empty:
            return "NO DATA"

        close = data["Close"]

        # yfinance MultiIndex support
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        last = float(close.iloc[-1])
        prev = float(close.iloc[-2])

        if last > prev:
            return "BULLISH"

        elif last < prev:
            return "BEARISH"

        return "SIDEWAYS"
