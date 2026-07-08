from datetime import datetime


class BacktestEngine:
    """
    Falcon Signal Pro AI V3.28.0
    Historical Backtesting Engine
    """

    def __init__(self):
        self.version = "V3.28.0"

    def run(self, candles, strategy=None):

        if not candles:
            return {
                "trades": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0,
                "net_profit": 0,
                "engine": self.version
            }

        trades = 0
        wins = 0
        losses = 0
        profit = 0

        for candle in candles:

            signal = candle.get("signal")

            if signal is None:
                continue

            trades += 1

            pnl = candle.get("profit", 0)

            profit += pnl

            if pnl >= 0:
                wins += 1
            else:
                losses += 1

        win_rate = (
            round((wins / trades) * 100, 2)
            if trades else 0
        )

        return {
            "trades": trades,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "net_profit": round(profit, 2),
            "strategy": strategy,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


backtest_engine = BacktestEngine()
