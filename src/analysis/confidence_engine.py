"""
Falcon Signal Pro AI V2.0
Confidence Engine V2
"""

class ConfidenceEngine:

    def calculate(self, result, pattern, volume, breakout):

        score = 0

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

        confidence = int((score / 7) * 100)

        if confidence >= 80:
            grade = "A+"

        elif confidence >= 65:
            grade = "A"

        elif confidence >= 50:
            grade = "B"

        else:
            grade = "C"

        return {
            "score": score,
            "confidence": confidence,
            "grade": grade
        }
