"""
Falcon Signal Pro AI V2.0
AI Score Engine V3
"""

class AIScoreEngine:

    def calculate(self, result, pattern, volume, breakout):

        score = 0
        max_score = 8

        if result["trend"] == "BULLISH":
            score += 1

        if result["ema"] == "BULLISH":
            score += 1

        if result["macd"] == "BULLISH":
            score += 1

        if "OVERSOLD" in result["rsi"]:
            score += 1

        if pattern != "NONE":
            score += 1

        if volume == "HIGH VOLUME":
            score += 1

        if breakout == "BULLISH BREAKOUT":
            score += 1

        if result["signal"] == "BUY":
            score += 1

        percent = round((score / max_score) * 100)

        if percent >= 85:
            grade = "A+"
        elif percent >= 70:
            grade = "A"
        elif percent >= 55:
            grade = "B"
        else:
            grade = "C"

        return {
            "score": score,
            "max_score": max_score,
            "percent": percent,
            "grade": grade
        }
