from datetime import datetime

from src.intelligence.intelligence_bridge import intelligence_bridge


class BacktestEngine:
    """
    Falcon Signal Pro AI V3.28.0
    Historical Backtesting Engine
    """

    def __init__(self):
        self.version = "V3.28.0"

    def run(
        self,
        candles,
        starting_balance=10000
    ):

        balance = starting_balance

        trades = 0
        wins = 0
        losses = 0

        history = []

        for candle in candles:

            result = intelligence_bridge.process(candle)

            decision = result["decision"]["decision"]

            profit = candle.get("profit", 0)

            if decision in [
                "BUY",
                "STRONG_BUY",
                "SELL",
                "STRONG_SELL"
            ]:

                trades += 1

                balance += profit

                if profit > 0:
                    wins += 1
                elif profit < 0:
                    losses += 1

                history.append(
                    {
                        "decision": decision,
                        "profit": profit,
                        "balance": balance
                    }
                )

        win_rate = (
            round((wins / trades) * 100, 2)
            if trades
            else 0
        )

        return {
            "starting_balance": starting_balance,
            "ending_balance": round(balance, 2),
            "net_profit": round(balance - starting_balance, 2),
            "trades": trades,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "history": history,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


backtest_engine = BacktestEngine()
