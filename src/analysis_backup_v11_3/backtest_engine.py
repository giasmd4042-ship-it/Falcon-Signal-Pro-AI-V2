"""
Falcon Signal Pro AI V2.0
Backtest Engine V1
"""

import pandas as pd


class BacktestEngine:

    def run(self, data: pd.DataFrame):

        if data.empty or len(data) < 2:
            return None

        close = data["Close"]

        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        wins = 0
        losses = 0

        for i in range(1, len(close)):
            if close.iloc[i] > close.iloc[i - 1]:
                wins += 1
            else:
                losses += 1

        total = wins + losses

        win_rate = (wins / total) * 100 if total else 0

        return {
            "wins": wins,
            "losses": losses,
            "total": total,
            "win_rate": round(win_rate, 2)
        }
