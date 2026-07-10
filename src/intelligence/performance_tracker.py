from datetime import datetime

from src.intelligence.memory_storage import memory_storage


class PerformanceTracker:
    """
    Falcon Signal Pro AI V3.26.1
    Pattern performance intelligence layer
    """

    def __init__(self):
        self.version = "V3.26.1"


    def record_result(
        self,
        pattern,
        signal,
        result,
        confidence=0,
        profit=0
    ):

        data = {
            "type": "trade_result",
            "pattern": pattern,
            "signal": signal,
            "result": result,
            "confidence": confidence,
            "profit": profit,
            "timestamp": datetime.now().isoformat()
        }

        return memory_storage.save(data)



    def _trades(self):

        history = memory_storage.load()

        return [
            item.get("data", {})
            for item in history
            if item.get("data", {}).get("type") == "trade_result"
        ]



    def get_statistics(self):

        trades = self._trades()

        total = len(trades)

        wins = [
            t for t in trades
            if t.get("result") == "WIN"
        ]

        losses = [
            t for t in trades
            if t.get("result") == "LOSS"
        ]


        win_rate = (
            round((len(wins) / total) * 100, 2)
            if total
            else 0
        )


        total_profit = sum(
            t.get("profit", 0)
            for t in trades
        )


        return {
            "total_trades": total,
            "wins": len(wins),
            "losses": len(losses),
            "win_rate": win_rate,
            "total_profit": round(total_profit, 2),
            "engine": self.version
        }



    def pattern_performance(self, pattern):

        trades = [
            t for t in self._trades()
            if t.get("pattern") == pattern
        ]

        total = len(trades)

        wins = len([
            t for t in trades
            if t.get("result") == "WIN"
        ])


        win_rate = (
            round((wins / total) * 100, 2)
            if total
            else 0
        )


        return {
            "pattern": pattern,
            "trades": total,
            "wins": wins,
            "win_rate": win_rate,
            "engine": self.version
        }



performance_tracker = PerformanceTracker()
