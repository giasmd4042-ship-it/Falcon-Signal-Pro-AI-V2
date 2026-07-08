"""
Falcon Signal Pro AI V2.0
Risk Manager
"""

class RiskManager:

    def calculate(self, balance, risk_percent, entry, stop_loss):

        risk_amount = balance * (risk_percent / 100)

        stop_distance = abs(entry - stop_loss)

        if stop_distance == 0:
            return None

        position_size = risk_amount / stop_distance

        return {
            "balance": round(balance, 2),
            "risk_percent": risk_percent,
            "risk_amount": round(risk_amount, 2),
            "position_size": round(position_size, 4)
        }
