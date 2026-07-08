from src.intelligence.decision_engine import decision_engine
from src.intelligence.market_memory import market_memory
from src.intelligence.pattern_memory import pattern_memory
from src.intelligence.reasoning_engine import reasoning_engine
from src.intelligence.memory_storage import memory_storage


class IntelligenceBridge:
    """
    Falcon Signal Pro AI V3.25.2
    Full intelligence integration bridge
    """

    def __init__(self):
        self.version = "V3.25.2"

    def process(self, market_state):

        memory = market_memory.store(market_state)

        persistent = memory_storage.save({
            "type": "market_state",
            "state": market_state
        })

        decision = decision_engine.evaluate(market_state)

        reasoning = reasoning_engine.analyze(decision)

        pattern = pattern_memory.save_pattern(
            decision.get("decision"),
            reasoning.get("reasoning"),
            decision.get("confidence", 0)
        )

        return {
            "memory": memory,
            "persistent_memory": persistent,
            "decision": decision,
            "reasoning": reasoning,
            "pattern": pattern,
            "engine": self.version
        }


intelligence_bridge = IntelligenceBridge()
