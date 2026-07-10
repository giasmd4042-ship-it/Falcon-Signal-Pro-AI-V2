from datetime import datetime

from src.portfolio.trade_journal import trade_journal


class PerformanceAnalytics:
    """
    Falcon Signal Pro AI V3.34.4
    AI Performance Analytics Engine
    """

    def __init__(self):
        self.version = "V3.34.4"


    def analyze(self):

        journal = trade_journal.history()

        trades = journal.get(
            "trades",
            []
        )


        total_profit = 0
        wins = 0
        losses = 0

        strategies = {}
        regimes = {}


        for item in trades:

            data = item.get(
                "data",
                {}
            )

            profit = data.get(
                "profit",
                0
            )

            strategy = data.get(
                "strategy",
                "UNKNOWN"
            )

            regime = data.get(
                "regime",
                "UNKNOWN"
            )


            total_profit += profit


            if profit > 0:
                wins += 1
            else:
                losses += 1


            if strategy not in strategies:
                strategies[strategy] = {
                    "trades": 0,
                    "profit": 0,
                    "wins": 0
                }


            strategies[strategy]["trades"] += 1
            strategies[strategy]["profit"] += profit


            if profit > 0:
                strategies[strategy]["wins"] += 1


            if regime not in regimes:
                regimes[regime] = {
                    "trades": 0,
                    "profit": 0
                }


            regimes[regime]["trades"] += 1
            regimes[regime]["profit"] += profit



        total = len(trades)

        win_rate = (
            round(
                (wins / total) * 100,
                2
            )
            if total
            else 0
        )


        best_strategy = None

        if strategies:
            best_strategy = max(
                strategies,
                key=lambda x: strategies[x]["profit"]
            )


        return {
            "total_trades": total,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "total_profit": total_profit,
            "strategies": strategies,
            "regimes": regimes,
            "best_strategy": best_strategy,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


performance_analytics = PerformanceAnalytics()
