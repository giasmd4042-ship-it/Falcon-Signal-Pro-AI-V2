"""
Falcon Signal Pro AI V7
Signal Strength Engine
"""

class SignalStrength:

    def calculate(
        self,
        trend,
        ema,
        rsi,
        macd,
        pattern,
        confidence,
    ):

        score = 0

        details = []

        # Trend
        if trend == "BULLISH":
            score += 2
            details.append("Bullish Trend")
        elif trend == "BEARISH":
            score += 2
            details.append("Bearish Trend")

        # EMA
        if ema == "BULLISH":
            score += 2
            details.append("EMA Confirmed")

        # RSI
        if "OVERSOLD" in str(rsi):
            score += 1
            details.append("RSI Oversold")

        elif "OVERBOUGHT" in str(rsi):
            score += 1
            details.append("RSI Overbought")

        # MACD
        if macd == "BULLISH":
            score += 2
            details.append("MACD Confirmed")

        # Pattern
        if pattern != "NONE":
            score += 1
            details.append(pattern)

        # Confidence
        if confidence >= 80:
            score += 2
        elif confidence >= 70:
            score += 1

        return {
            "score": score,
            "max_score": 10,
            "details": details
        }
