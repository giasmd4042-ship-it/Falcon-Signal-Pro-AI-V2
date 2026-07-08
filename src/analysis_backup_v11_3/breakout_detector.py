"""
Falcon Signal Pro AI V2.0
Breakout Detector
"""

import pandas as pd


class BreakoutDetector:

    def detect(self, data: pd.DataFrame):

        if data.empty or len(data) < 20:
            return "NO DATA"

        def series(col):
            s = data[col]
            if isinstance(s, pd.DataFrame):
                s = s.iloc[:, 0]
            return s

        high = series("High")
        low = series("Low")
        close = series("Close")

        resistance = float(high.tail(20).max())
        support = float(low.tail(20).min())
        last = float(close.iloc[-1])

        if last > resistance:
            return "BULLISH BREAKOUT"

        elif last < support:
            return "BEARISH BREAKOUT"

        return "NO BREAKOUT"
