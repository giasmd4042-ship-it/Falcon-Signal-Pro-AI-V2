from src.intelligence.decision_engine import decision_engine
from src.intelligence.market_memory import market_memory
from src.intelligence.pattern_memory import pattern_memory
from src.intelligence.reasoning_engine import reasoning_engine


class IntelligenceBridge:
    """
    Falcon Signal Pro AI V3.25
    Connect analysis engine with intelligence layer
    """

    def __init__(self):
        self.version = "V3.25.0"

    def process(self, market_state):
        memory = market_memory.store(market_state)

        decision = decision_engine.evaluate(market_state)

        reasoning = reasoning_engine.analyze(decision)

        pattern_memory.save_pattern(
            decision.get("decision"),
            reasoning.get("reasoning"),
            decision.get("confidence", 0)
        )

        return {
            "memory": memory,
            "decision": decision,
            "reasoning": reasoning,
            "engine": self.version
        }


intelligence_bridge = IntelligenceBridge()
