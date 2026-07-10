from datetime import datetime


class StrategyBenchmark:
    """
    Falcon Signal Pro AI V3.29.2
    Strategy Benchmark Engine
    """

    def __init__(self):
        self.version = "V3.29.2"

    def rank(self, strategies):

        if not strategies:
            return {
                "ranking": [],
                "engine": self.version
            }

        ranked = []

        for strategy in strategies:

            win_rate = strategy.get(
                "win_rate",
                0
            )

            profit_factor = strategy.get(
                "profit_factor",
                0
            )

            risk_score = strategy.get(
                "risk_score",
                0
            )


            score = round(
                (win_rate * 0.5)
                +
                (profit_factor * 20)
                +
                (risk_score * 0.3),
                2
            )


            ranked.append({
                "strategy": strategy.get(
                    "name",
                    "Unknown"
                ),
                "score": score
            })


        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return {
            "ranking": ranked,
            "best_strategy": ranked[0]["strategy"],
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


strategy_benchmark = StrategyBenchmark()
