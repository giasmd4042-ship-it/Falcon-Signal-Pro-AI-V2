from datetime import datetime


class StrategyOptimizer:
    """
    Falcon Signal Pro AI V3.27.4
    Strategy Optimizer Engine
    """

    def __init__(self):
        self.version = "V3.27.4"

    def optimize(self, strategies):

        if not strategies:
            return {
                "selected_strategy": None,
                "score": 0,
                "reason": "No strategies available",
                "engine": self.version
            }

        ranked = sorted(
            strategies,
            key=lambda s: (
                s.get("win_rate", 0),
                s.get("profit_factor", 0),
                s.get("confidence", 0)
            ),
            reverse=True
        )

        best = ranked[0]

        score = round(
            (
                best.get("win_rate", 0) * 0.5 +
                best.get("profit_factor", 0) * 20 +
                best.get("confidence", 0) * 0.3
            ),
            2
        )

        return {
            "selected_strategy": best.get("name"),
            "score": score,
            "details": best,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


strategy_optimizer = StrategyOptimizer()
