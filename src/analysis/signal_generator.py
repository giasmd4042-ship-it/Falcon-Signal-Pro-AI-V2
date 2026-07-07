"""
Falcon Signal Pro AI V2.0
Signal Generator
"""

from src.analysis.trend_analyzer import TrendAnalyzer
from src.analysis.ema_analyzer import EMAAnalyzer
from src.analysis.rsi_analyzer import RSIAnalyzer
from src.analysis.macd_analyzer import MACDAnalyzer


class SignalGenerator:

    def __init__(self):
        self.trend = TrendAnalyzer()
        self.ema = EMAAnalyzer()
        self.rsi = RSIAnalyzer()
        self.macd = MACDAnalyzer()

    def generate(self, data):

        trend = self.trend.detect_trend(data)
        ema = self.ema.detect(data)
        rsi = self.rsi.detect(data)
        macd = self.macd.detect(data)

        bullish = 0
        bearish = 0

        for value in (trend, ema, macd):
            if value == "BULLISH":
                bullish += 1
            elif value == "BEARISH":
                bearish += 1

        if "OVERSOLD" in rsi:
            bullish += 1
        elif "OVERBOUGHT" in rsi:
            bearish += 1

        total = bullish + bearish
        confidence = int(max(bullish, bearish) / total * 100) if total else 0

        if bullish > bearish:
            signal = "BUY"
        elif bearish > bullish:
            signal = "SELL"
        else:
            signal = "HOLD"

        return {
            "trend": trend,
            "ema": ema,
            "rsi": rsi,
            "macd": macd,
            "signal": signal,
            "confidence": confidence,
        }
