from datetime import datetime

from src.intelligence.memory_storage import memory_storage


class TradeFeedback:
    """
    Falcon Signal Pro AI V3.26.0
    Auto learning feedback loop
    """

    def __init__(self):
        self.version = "V3.26.0"


    def record_result(
        self,
        signal,
        entry,
        exit_price,
        result
    ):

        profit = exit_price - entry

        if signal == "SELL":
            profit = entry - exit_price


        feedback = {
            "type": "trade_result",
            "signal": signal,
            "entry": entry,
            "exit": exit_price,
            "profit": round(profit, 2),
            "result": result,
            "timestamp": datetime.now().isoformat()
        }


        memory_storage.save(feedback)

        return feedback



    def statistics(self):

        history = memory_storage.get_history()

        wins = 0
        losses = 0


        for item in history:

            data = item.get(
                "data",
                {}
            )

            if data.get("type") == "trade_result":

                if data.get("result") == "WIN":
                    wins += 1

                elif data.get("result") == "LOSS":
                    losses += 1


        total = wins + losses

        win_rate = 0

        if total:
            win_rate = round(
                (wins / total) * 100,
                2
            )


        return {
            "wins": wins,
            "losses": losses,
            "total": total,
            "win_rate": win_rate,
            "engine": self.version
        }


trade_feedback = TradeFeedback()
