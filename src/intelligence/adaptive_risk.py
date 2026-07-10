from datetime import datetime


class AdaptiveRiskEngine:
    """
    Falcon Signal Pro AI V3.27.3
    Adaptive Risk Management Engine
    """

    def __init__(self):
        self.version = "V3.27.3"


    def calculate(
        self,
        balance,
        risk_percent,
        entry,
        atr,
        confidence,
        regime
    ):

        base_risk = balance * (risk_percent / 100)

        risk_multiplier = 1.0

        regime = str(regime).upper()


        if regime == "HIGH_VOLATILITY":
            risk_multiplier = 0.70

        elif regime == "LOW_VOLATILITY":
            risk_multiplier = 1.10

        elif regime == "TRENDING":
            risk_multiplier = 1.20


        if confidence >= 85:
            confidence_multiplier = 1.15

        elif confidence <= 50:
            confidence_multiplier = 0.80

        else:
            confidence_multiplier = 1.0


        final_risk = (
            base_risk
            * risk_multiplier
            * confidence_multiplier
        )


        stop_distance = atr * 1.5

        take_profit_distance = (
            stop_distance * 2
        )


        stop_loss = entry - stop_distance

        take_profit = (
            entry + take_profit_distance
        )


        return {
            "risk_amount": round(final_risk, 2),
            "risk_multiplier": risk_multiplier,
            "confidence_multiplier": confidence_multiplier,
            "stop_loss": round(stop_loss, 2),
            "take_profit": round(take_profit, 2),
            "risk_reward": "1:2",
            "regime": regime,
            "engine": self.version,
            "timestamp": datetime.now().isoformat()
        }


adaptive_risk = AdaptiveRiskEngine()
