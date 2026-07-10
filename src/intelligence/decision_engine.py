from datetime import datetime

from src.intelligence.memory_storage import memory_storage
from src.intelligence.confidence_learning import confidence_learning


class DecisionEngine:
    """
    Falcon Signal Pro AI V3.25.5
    Adaptive confidence learning decision layer
    """

    def __init__(self):
        self.version = "V3.25.5"
        self.created_at = datetime.now()


    def evaluate(self, market_state):

        if not market_state:
            return {
                "decision": "WAIT",
                "confidence": 0,
                "reason": "No market data",
                "engine": self.version
            }


        base_confidence = market_state.get(
            "score",
            market_state.get("confidence", 0)
        )


        history = memory_storage.get_history()


        total = 0
        wins = 0


        for item in history:

            result = item.get(
                "data",
                {}
            ).get(
                "result"
            )

            if result:

                total += 1

                if result == "WIN":
                    wins += 1


        win_rate = 0

        if total:
            win_rate = int(
                (wins / total) * 100
            )


        learning = confidence_learning.adjust(
            base_confidence,
            {
                "win_rate": win_rate
            }
        )


        confidence = learning[
            "adjusted_confidence"
        ]


        if confidence >= 80:
            decision = "STRONG_BUY"

        elif confidence >= 60:
            decision = "BUY"

        elif confidence <= 20:
            decision = "STRONG_SELL"

        elif confidence <= 40:
            decision = "SELL"

        else:
            decision = "WAIT"


        return {
            "decision": decision,
            "confidence": confidence,
            "base_confidence": base_confidence,
            "learning": learning,
            "historical_win_rate": win_rate,
            "reason": "AI adaptive evaluation with confidence learning",
            "engine": self.version
        }


decision_engine = DecisionEngine()
