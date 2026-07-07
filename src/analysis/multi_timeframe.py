"""
Falcon Signal Pro AI V2.0
Multi Timeframe Analyzer
"""

from src.analysis.market_data import MarketData
from src.analysis.trend_analyzer import TrendAnalyzer


class MultiTimeframeAnalyzer:

    def __init__(self):
        self.market = MarketData()
        self.trend = TrendAnalyzer()

    def analyze(self, symbol):

        frames = {
            "15m": ("15m", "5d"),
            "1h": ("1h", "7d"),
            "4h": ("4h", "30d"),
            "1d": ("1d", "6mo"),
        }

        result = {}

        bullish = 0
        bearish = 0

        for name, (interval, period) in frames.items():

            data = self.market.get_data(
                symbol,
                interval=interval,
                period=period
            )

            trend = self.trend.detect_trend(data)

            result[name] = trend

            if trend == "BULLISH":
                bullish += 1
            elif trend == "BEARISH":
                bearish += 1

        if bullish > bearish:
            overall = "BULLISH"
        elif bearish > bullish:
            overall = "BEARISH"
        else:
            overall = "SIDEWAYS"

        result["overall"] = overall
        result["score"] = f"{max(bullish, bearish)}/4"

        return result

