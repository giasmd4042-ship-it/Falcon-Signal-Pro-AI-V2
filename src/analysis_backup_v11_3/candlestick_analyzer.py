"""
Falcon Signal Pro AI V2.0
Candlestick Pattern Analyzer
"""

import pandas as pd


class CandlestickAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty or len(data) < 2:
            return "NO DATA"

        def get_series(column):
            s = data[column]
            if isinstance(s, pd.DataFrame):
                s = s.iloc[:, 0]
            return s

        open_ = get_series("Open")
        high = get_series("High")
        low = get_series("Low")
        close = get_series("Close")

        o = float(open_.iloc[-1])
        h = float(high.iloc[-1])
        l = float(low.iloc[-1])
        c = float(close.iloc[-1])

        po = float(open_.iloc[-2])
        pc = float(close.iloc[-2])

        body = abs(c - o)
        candle = h - l

        # Doji
        if candle > 0 and body / candle <= 0.10:
            return "DOJI"

        # Bullish Engulfing
        if pc < po and c > o and c >= po and o <= pc:
            return "BULLISH ENGULFING"

        # Bearish Engulfing
        if pc > po and c < o and c <= po and o >= pc:
            return "BEARISH ENGULFING"

        # Hammer
        lower_shadow = min(o, c) - l
        upper_shadow = h - max(o, c)

        if lower_shadow > body * 2 and upper_shadow < body:
            return "HAMMER"

        return "NONE"
