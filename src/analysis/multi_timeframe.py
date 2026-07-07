"""
Falcon Signal Pro AI V9
Multi Timeframe Analyzer
"""

from src.analysis.market_data import MarketData
from src.analysis.trend_analyzer import TrendAnalyzer


class MultiTimeframeAnalyzer:

    def __init__(self):
        self.market = MarketData()
        self.trend = TrendAnalyzer()

    def analyze(self, symbol):

        timeframes = [
            "15m",
            "1h",
            "4h",
            "1d"
        ]

        result = {}

        bullish = 0
        bearish = 0

        for tf in timeframes:

            try:
                data = self.market.get_data(
                    symbol=symbol,
                    interval=tf
                )

                trend = self.trend.detect_trend(data)

                result[tf] = trend

                if trend == "BULLISH":
                    bullish += 1
                elif trend == "BEARISH":
                    bearish += 1

            except Exception:
                result[tf] = "ERROR"

        if bullish > bearish:
            overall = "BULLISH"
        elif bearish > bullish:
            overall = "BEARISH"
        else:
            overall = "NEUTRAL"

        result["overall"] = overall

        return result
