from datetime import datetime


class DecisionEngine:
    """
    Falcon Signal Pro AI V3.25
    Intelligence decision layer
    """

    def __init__(self):
        self.version = "V3.25.0"
        self.created_at = datetime.now()

    def evaluate(self, market_state):
        """
        Evaluate market intelligence state
        """

        if not market_state:
            return {
                "decision": "WAIT",
                "confidence": 0,
                "reason": "No market data"
            }

        score = market_state.get("score", 0)

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

        return {
            "decision": decision,
            "confidence": score,
            "reason": "AI intelligence evaluation",
            "engine": self.version
        }


decision_engine = DecisionEngine()
