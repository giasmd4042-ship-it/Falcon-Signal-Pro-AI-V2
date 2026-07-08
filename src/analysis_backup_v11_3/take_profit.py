"""
Falcon Signal Pro AI V2.0
Take Profit Calculator
"""

class TakeProfitCalculator:

    def calculate(self, entry, stop_loss, rr=2.0):

        risk = abs(entry - stop_loss)

        if entry > stop_loss:
            take_profit = entry + (risk * rr)
        else:
            take_profit = entry - (risk * rr)

        return {
            "entry": round(entry, 2),
            "stop_loss": round(stop_loss, 2),
            "take_profit": round(take_profit, 2),
            "risk_reward": f"1:{rr}"
        }
