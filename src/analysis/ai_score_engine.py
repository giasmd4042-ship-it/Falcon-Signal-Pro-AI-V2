"""
Falcon Signal Pro AI V2
AI Score Engine
"""

class AIScoreEngine:

    def calculate(self, result, pattern, volume="NORMAL VOLUME", breakout="NO BREAKOUT"):

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

        if breakout != "NO BREAKOUT":
            score += 1

        if result["signal"] == "BUY":
            score += 1

        percent = int((score / max_score) * 100)

        if percent >= 90:
            grade = "A+"
        elif percent >= 75:
            grade = "A"
        elif percent >= 60:
            grade = "B"
        elif percent >= 40:
            grade = "C"
        else:
            grade = "D"

        return {
            "score": score,
            "max_score": max_score,
            "percent": percent,
            "grade": grade
        }
