from datetime import datetime

from src.intelligence.market_memory import market_memory
from src.intelligence.memory_storage import memory_storage
from src.intelligence.decision_engine import decision_engine
from src.intelligence.reasoning_engine import reasoning_engine
from src.intelligence.market_regime import market_regime
from src.intelligence.strategy_optimizer import strategy_optimizer
from src.intelligence.adaptive_risk import adaptive_risk


class IntelligenceBridge:
    """
    Falcon Signal Pro AI V3.27.5
    Unified Intelligence Bridge
    """

    def __init__(self):
        self.version = "V3.27.5"

    def process(self, market_state):

        memory = market_memory.store(market_state)

        persistent = memory_storage.save({
            "type": "market_state",
            "state": market_state
        })

        regime = market_regime.detect(market_state)

        decision = decision_engine.evaluate(market_state)

        strategies = market_state.get("strategies", [])

        strategy = strategy_optimizer.optimize(strategies)

        risk = adaptive_risk.calculate(
            account_balance=market_state.get("balance", 10000),
            risk_percent=market_state.get("risk_percent", 2),
            entry=market_state.get("entry", 0),
            atr=market_state.get("atr", 100),
            confidence=decision["confidence"],
            regime=regime["regime"]
        )

        reasoning = reasoning_engine.analyze(decision)

        return {
            "memory": memory,
            "persistent_memory": persistent,
            "regime": regime,
            "decision": decision,
            "strategy": strategy,
            "risk": risk,
            "reasoning": reasoning,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


intelligence_bridge = IntelligenceBridge()
