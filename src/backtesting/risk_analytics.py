from datetime import datetime


class RiskAnalytics:
    """
    Falcon Signal Pro AI V3.29.1
    Drawdown & Risk Analytics Engine
    """

    def __init__(self):
        self.version = "V3.29.1"

    def analyze(self, equity_curve):

        if not equity_curve:
            return {
                "max_drawdown": 0,
                "recovery_factor": 0,
                "risk_score": 0,
                "engine": self.version
            }

        peak = equity_curve[0]
        max_drawdown = 0

        for value in equity_curve:

            if value > peak:
                peak = value

            drawdown = peak - value

            if drawdown > max_drawdown:
                max_drawdown = drawdown

        net_profit = equity_curve[-1] - equity_curve[0]

        recovery_factor = (
            round(net_profit / max_drawdown, 2)
            if max_drawdown else 999
        )

        risk_score = max(
            0,
            round(100 - (max_drawdown / peak) * 100, 2)
        )

        return {
            "max_drawdown": round(max_drawdown, 2),
            "recovery_factor": recovery_factor,
            "risk_score": risk_score,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


risk_analytics = RiskAnalytics()
