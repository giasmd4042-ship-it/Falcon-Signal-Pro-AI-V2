"""
Falcon Signal Pro AI V11.3
Volatility Analyzer
"""

import pandas as pd


class VolatilityAnalyzer:

    def analyze(self, data: pd.DataFrame):

        if data.empty or len(data) < 14:
            return {
                "atr": 0,
                "level": "UNKNOWN",
                "risk": "UNKNOWN"
            }

        high = data["High"]
        low = data["Low"]
        close = data["Close"]

        tr1 = high - low
        tr2 = (high - close.shift()).abs()
        tr3 = (low - close.shift()).abs()

        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = float(tr.rolling(14).mean().iloc[-1])

        if atr < 150:
            level = "LOW"
            risk = "LOW"

        elif atr < 300:
            level = "MEDIUM"
            risk = "NORMAL"

        else:
            level = "HIGH"
            risk = "HIGH"

        return {
            "atr": round(atr, 2),
            "level": level,
            "risk": risk
        }
