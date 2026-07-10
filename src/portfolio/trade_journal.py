from datetime import datetime
from src.intelligence.memory_storage import memory_storage


class TradeJournal:
    """
    Falcon Signal Pro AI V3.31.1
    AI Trade Journal Engine
    """

    def __init__(self):
        self.version = "V3.31.1"


    def record(
        self,
        symbol,
        side,
        entry,
        exit_price,
        profit,
        strategy,
        confidence,
        regime
    ):

        trade = {
            "type": "trade_journal",
            "symbol": symbol,
            "side": side,
            "entry": entry,
            "exit": exit_price,
            "profit": profit,
            "strategy": strategy,
            "confidence": confidence,
            "regime": regime,
            "timestamp": datetime.now().isoformat()
        }


        return memory_storage.save(
            trade
        )


    def history(self):

        data = memory_storage.load()

        trades = [
            item
            for item in data
            if item.get("data", {}).get(
                "type"
            ) == "trade_journal"
        ]

        return {
            "total_trades": len(trades),
            "trades": trades,
            "engine": self.version
        }


    def performance(self):

        journal = self.history()

        trades = journal["trades"]

        total_profit = sum(
            item["data"].get(
                "profit",
                0
            )
            for item in trades
        )

        wins = len(
            [
                item for item in trades
                if item["data"].get("profit",0) > 0
            ]
        )


        win_rate = (
            round(
                (wins / len(trades)) * 100,
                2
            )
            if trades
            else 0
        )


        return {
            "total_trades": len(trades),
            "wins": wins,
            "win_rate": win_rate,
            "total_profit": total_profit,
            "engine": self.version
        }


trade_journal = TradeJournal()
