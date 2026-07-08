"""
Falcon Signal Pro AI V2.0
RSI Analyzer
"""

import pandas as pd


class RSIAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty:
            return "NO DATA"

        close = data["Close"]

        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        delta = close.diff()

        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()

        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        last = float(rsi.iloc[-1])

        if last > 70:
            return f"OVERBOUGHT ({last:.2f})"

        elif last < 30:
            return f"OVERSOLD ({last:.2f})"

        return f"NEUTRAL ({last:.2f})"
