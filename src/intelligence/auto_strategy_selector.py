from datetime import datetime


class AutoStrategySelector:
    """
    Falcon Signal Pro AI V3.30.1
    AI Auto Strategy Selector
    """

    def __init__(self):
        self.version = "V3.30.1"

    def select(
        self,
        benchmark,
        regime,
        confidence,
        risk
    ):

        ranking = benchmark.get(
            "ranking",
            []
        )

        if not ranking:
            return {
                "active_strategy": None,
                "reason": "No strategies available",
                "engine": self.version
            }

        selected = ranking[0]["strategy"]

        risk_amount = risk.get(
            "risk_amount",
            0
        )

        regime = str(regime).upper()

        if regime == "HIGH_VOLATILITY" and len(ranking) > 1:
            selected = ranking[1]["strategy"]

        if confidence < 60:
            status = "SAFE_MODE"
        else:
            status = "ACTIVE"

        return {
            "active_strategy": selected,
            "status": status,
            "confidence": confidence,
            "regime": regime,
            "risk_amount": risk_amount,
            "reason": f"Selected using benchmark ranking under {regime}",
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


auto_strategy_selector = AutoStrategySelector()
