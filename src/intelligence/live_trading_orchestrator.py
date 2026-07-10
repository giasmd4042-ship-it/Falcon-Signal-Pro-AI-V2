from datetime import datetime

from src.intelligence.market_regime import market_regime
from src.intelligence.decision_engine import decision_engine
from src.intelligence.adaptive_risk import adaptive_risk
from src.intelligence.auto_strategy_selector import auto_strategy_selector
from src.intelligence.strategy_optimizer import strategy_optimizer


class LiveTradingOrchestrator:
    """
    Falcon Signal Pro AI V3.30.2
    Live Trading Intelligence Orchestrator
    """

    def __init__(self):
        self.version = "V3.30.2"


    def execute(self, market):

        regime = market_regime.detect(
            market
        )


        decision = decision_engine.evaluate(
            market
        )


        strategy = strategy_optimizer.optimize(
            market.get(
                "strategies",
                []
            )
        )


        selected_strategy = auto_strategy_selector.select(
            {
                "ranking": [
                    {
                        "strategy": strategy.get(
                            "selected_strategy"
                        ),
                        "score": strategy.get(
                            "score",
                            0
                        )
                    }
                ]
            },
            regime.get(
                "regime"
            ),
            decision.get(
                "confidence"
            ),
            {}
        )


        risk = adaptive_risk.calculate(
            market.get(
                "balance",
                0
            ),
            market.get(
                "risk_percent",
                1
            ),
            market.get(
                "entry",
                0
            ),
            market.get(
                "atr",
                0
            ),
            decision.get(
                "confidence",
                0
            ),
            regime.get(
                "regime"
            )
        )


        return {
            "signal": decision.get(
                "decision"
            ),
            "confidence": decision.get(
                "confidence"
            ),
            "regime": regime,
            "strategy": selected_strategy,
            "risk": risk,
            "ready_for_execution": (
                decision.get("confidence", 0) >= 70
            ),
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


live_trading_orchestrator = LiveTradingOrchestrator()
