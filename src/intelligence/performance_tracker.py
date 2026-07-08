from datetime import datetime
from src.intelligence.memory_storage import memory_storage


class PerformanceTracker:
    """
    Falcon Signal Pro AI V3.25.3
    Pattern WIN/LOSS learning layer
    """

    def __init__(self):
        self.version = "V3.25.3"

    def record_result(
        self,
        pattern,
        signal,
        result,
        confidence=0
    ):

        data = {
            "type": "trade_result",
            "pattern": pattern,
            "signal": signal,
            "result": result,
            "confidence": confidence,
            "timestamp": datetime.now().isoformat()
        }

        return memory_storage.save(data)


    def get_statistics(self):

        history = memory_storage.load()

        trades = [
            item
            for item in history
            if item.get("data", {}).get("type") == "trade_result"
        ]

        total = len(trades)

        wins = len([
            item for item in trades
            if item["data"].get("result") == "WIN"
        ])

        losses = len([
            item for item in trades
            if item["data"].get("result") == "LOSS"
        ])

        win_rate = (
            round((wins / total) * 100, 2)
            if total
            else 0
        )

        return {
            "total_trades": total,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
            "engine": self.version
        }


performance_tracker = PerformanceTracker()
