from datetime import datetime

from src.portfolio.trade_journal import trade_journal


class PerformanceAnalytics:
    """
    Falcon Signal Pro AI V3.71
    AI Performance Analytics Engine
    """

    def __init__(self):
        self.version = "V3.71"


    def analyze(self):

        journal = trade_journal.history()

        trades = journal.get(
            "trades",
            []
        )


        total_profit = 0
        wins = 0
        losses = 0
        gross_profit = 0
        gross_loss = 0
        winning_trades = 0
        losing_trades = 0

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
                gross_profit += profit
                winning_trades += 1

            else:
                losses += 1
                gross_loss += abs(profit)
                losing_trades += 1


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

        average_win = (
            round(
                gross_profit / winning_trades,
                2
            )
            if winning_trades
            else 0
        )

        average_loss = (
            round(
                gross_loss / losing_trades,
                2
            )
            if losing_trades
            else 0
        )

        if gross_loss:
            profit_factor = round(
                gross_profit / gross_loss,
                2
            )

        elif gross_profit:
            profit_factor = "INF"

        else:
            profit_factor = 0
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
            "average_win": average_win,
            "average_loss": average_loss,
            "profit_factor": profit_factor,
            "total_profit": total_profit,
            "strategies": strategies,
            "regimes": regimes,
            "best_strategy": best_strategy,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


performance_analytics = PerformanceAnalytics()
