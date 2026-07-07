"""
Falcon Signal Pro AI V9.1
AI Score Engine
"""

class AIScoreEngine:

    def calculate(
        self,
        result,
        pattern,
        volume="NORMAL VOLUME",
        breakout="NO BREAKOUT"
    ):

        confidence = int(result.get("confidence", 0))
        signal = result.get("signal", "HOLD")

        # Base score = confidence
        score = confidence

        # Trend alignment
        if signal == "BUY" and result["trend"] == "BULLISH":
            score += 10
        elif signal == "SELL" and result["trend"] == "BEARISH":
            score += 10

        # EMA alignment
        if signal == "BUY" and result["ema"] == "BULLISH":
            score += 5
        elif signal == "SELL" and result["ema"] == "BEARISH":
            score += 5

        # MACD alignment
        if signal == "BUY" and result["macd"] == "BULLISH":
            score += 5
        elif signal == "SELL" and result["macd"] == "BEARISH":
            score += 5

        # Candlestick pattern
        if pattern != "NONE":
            score += 5

        # Volume
        if volume == "HIGH VOLUME":
            score += 5

        # Breakout
        if breakout != "NO BREAKOUT":
            score += 5

        # HOLD penalty
        if signal == "HOLD":
            score = min(score, 50)

        # Clamp score
        score = max(0, min(score, 100))

        if score >= 90:
            grade = "A+"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        else:
            grade = "D"

        return {
            "score": score,
            "max_score": 100,
            "percent": score,
            "grade": grade
        }
