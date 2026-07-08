from datetime import datetime


class ReasoningEngine:
    """
    Falcon Signal Pro AI V3.25
    AI reasoning and explanation layer
    """

    def __init__(self):
        self.version = "V3.25.0"

    def analyze(self, decision_data):
        if not decision_data:
            return {
                "reasoning": "No decision data available",
                "confidence": 0
            }

        confidence = decision_data.get("confidence", 0)
        decision = decision_data.get("decision", "WAIT")

        if confidence >= 80:
            explanation = "Strong market alignment detected"
        elif confidence >= 60:
            explanation = "Moderate confirmation detected"
        elif confidence <= 40:
            explanation = "Weak market condition detected"
        else:
            explanation = "Neutral market condition"

        return {
            "decision": decision,
            "confidence": confidence,
            "reasoning": explanation,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


reasoning_engine = ReasoningEngine()
