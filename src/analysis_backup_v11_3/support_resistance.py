"""
Falcon Signal Pro AI V2.0
Support & Resistance Analyzer
"""

import pandas as pd


class SupportResistanceAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty:
            return None

        high = data["High"]
        low = data["Low"]

        # yfinance MultiIndex support
        if isinstance(high, pd.DataFrame):
            high = high.iloc[:, 0]

        if isinstance(low, pd.DataFrame):
            low = low.iloc[:, 0]

        resistance = float(high.tail(20).max())
        support = float(low.tail(20).min())

        return {
            "support": round(support, 2),
            "resistance": round(resistance, 2),
        }
