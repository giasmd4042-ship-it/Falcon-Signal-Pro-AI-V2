"""
Falcon Signal Pro AI V3.25
Intelligent Signal Generator
"""

from src.analysis.trend_analyzer import TrendAnalyzer
from src.analysis.ema_analyzer import EMAAnalyzer
from src.analysis.rsi_analyzer import RSIAnalyzer
from src.analysis.macd_analyzer import MACDAnalyzer
from src.analysis.signal_strength import SignalStrength
from src.analysis.signal_filter import SignalFilter
from src.analysis.volume_analyzer import VolumeAnalyzer
from src.analysis.breakout_detector import BreakoutDetector

from src.intelligence.intelligence_bridge import IntelligenceBridge


class SignalGenerator:

    def __init__(self):

        self.trend = TrendAnalyzer()
        self.ema = EMAAnalyzer()
        self.rsi = RSIAnalyzer()
        self.macd = MACDAnalyzer()

        self.strength = SignalStrength()
        self.filter = SignalFilter()
        self.volume = VolumeAnalyzer()
        self.breakout = BreakoutDetector()

        self.intelligence = IntelligenceBridge()


    def generate(self, data):

        trend = self.trend.detect_trend(data)
        ema = self.ema.detect(data)
        rsi = self.rsi.detect(data)
        macd = self.macd.detect(data)
        volume = self.volume.detect(data)
        breakout = self.breakout.detect(data)

        bullish = 0
        bearish = 0

        for value in (trend, ema, macd):

            if value == "BULLISH":
                bullish += 1

            elif value == "BEARISH":
                bearish += 1


        if "OVERSOLD" in str(rsi):
            bullish += 1

        elif "OVERBOUGHT" in str(rsi):
            bearish += 1


        total = bullish + bearish

        confidence = (
            int(max(bullish, bearish) / total * 100)
            if total else 0
        )


        if bullish > bearish:
            signal = "BUY"

        elif bearish > bullish:
            signal = "SELL"

        else:
            signal = "HOLD"


        strength = self.strength.calculate(
            trend=trend,
            ema=ema,
            rsi=rsi,
            macd=macd,
            pattern="NONE",
            confidence=confidence,
        )


        validation = self.filter.validate(
            signal=signal,
            confidence=confidence,
            trend=trend,
            strength_score=strength["score"],
        )


        intelligence = self.intelligence.process(
            market_state={
                "trend": trend,
                "ema": ema,
                "rsi": rsi,
                "macd": macd,
                "volume": volume,
                "breakout": breakout,
                "signal": signal,
                "confidence": confidence,
            }
        )


        return {
            "trend": trend,
            "ema": ema,
            "rsi": rsi,
            "macd": macd,
            "volume": volume,
            "breakout": breakout,
            "signal": signal,
            "confidence": confidence,
            "strength": strength,
            "filter": validation,
            "intelligence": intelligence,
        }


signal_generator = SignalGenerator()
