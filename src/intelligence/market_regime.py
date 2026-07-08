from datetime import datetime


class MarketRegime:
    """
    Falcon Signal Pro AI V3.27.2
    Market Regime Detection Engine
    """

    def __init__(self):
        self.version = "V3.27.2"

    def detect(self, market_state):

        trend = str(
            market_state.get("trend", "")
        ).upper()

        atr = float(
            market_state.get("atr", 0)
        )

        volume = float(
            market_state.get("volume_ratio", 1)
        )

        regime = "RANGING"
        confidence = 60
        reason = "Sideways market"

        if atr >= 300:
            regime = "HIGH_VOLATILITY"
            confidence = 90
            reason = "ATR indicates high volatility"

        elif atr <= 100:
            regime = "LOW_VOLATILITY"
            confidence = 80
            reason = "ATR indicates low volatility"

        elif trend in ["BULLISH", "BEARISH"]:

            regime = "TRENDING"
            confidence = 85

            if volume >= 1:
                confidence += 5

            reason = f"{trend} trend confirmed"

        return {
            "regime": regime,
            "confidence": min(confidence, 100),
            "reason": reason,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


market_regime = MarketRegime()
