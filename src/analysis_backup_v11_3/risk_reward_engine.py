"""
Falcon Signal Pro AI V11.2
Risk Reward Engine
"""


class RiskRewardEngine:

    def calculate(self, entry, stop_loss, take_profit):

        risk = abs(entry - stop_loss)
        reward = abs(take_profit - entry)

        if risk == 0:
            ratio = 0
        else:
            ratio = round(reward / risk, 2)

        if ratio >= 3:
            quality = "EXCELLENT"

        elif ratio >= 2:
            quality = "GOOD"

        elif ratio >= 1.5:
            quality = "AVERAGE"

        else:
            quality = "POOR"

        return {
            "risk": round(risk, 2),
            "reward": round(reward, 2),
            "ratio": ratio,
            "quality": quality
        }
