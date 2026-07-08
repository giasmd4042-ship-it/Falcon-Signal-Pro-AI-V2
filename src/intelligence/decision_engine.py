from datetime import datetime

from src.intelligence.pattern_memory import pattern_memory


class DecisionEngine:
    """
    Falcon Signal Pro AI V3.25.2
    Historical intelligence decision layer
    """

    def __init__(self):
        self.version = "V3.25.2"
        self.created_at = datetime.now()

    def evaluate(self, market_state):

        if not market_state:
            return {
                "decision": "WAIT",
                "confidence": 0,
                "reason": "No market data",
                "engine": self.version
            }

        score = market_state.get(
            "score",
            market_state.get("confidence", 0)
        )

        if score >= 80:
            decision = "STRONG_BUY"

        elif score >= 60:
            decision = "BUY"

        elif score <= 20:
            decision = "STRONG_SELL"

        elif score <= 40:
            decision = "SELL"

        else:
            decision = "WAIT"


        previous = pattern_memory.find_patterns(decision)

        history_bonus = 0

        if len(previous) >= 3:
            history_bonus = 5

        adjusted_confidence = min(
            score + history_bonus,
            100
        )

        return {
            "decision": decision,
            "confidence": adjusted_confidence,
            "base_confidence": score,
            "historical_matches": len(previous),
            "reason": "AI intelligence evaluation with historical memory",
            "engine": self.version
        }


decision_engine = DecisionEngine()
