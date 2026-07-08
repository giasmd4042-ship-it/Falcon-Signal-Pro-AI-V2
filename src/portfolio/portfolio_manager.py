from datetime import datetime


class PortfolioManager:
    """
    Falcon Signal Pro AI V3.31.0
    AI Portfolio Management Engine
    """

    def __init__(self):
        self.version = "V3.31.0"


    def analyze(
        self,
        balance,
        positions,
        risk_limit=10
    ):

        total_exposure = 0
        active_positions = len(
            positions
        )

        allocation = []


        for position in positions:

            amount = position.get(
                "amount",
                0
            )

            total_exposure += amount

            allocation.append(
                {
                    "symbol": position.get(
                        "symbol",
                        "UNKNOWN"
                    ),
                    "allocation": round(
                        (amount / balance) * 100,
                        2
                    ) if balance else 0
                }
            )


        exposure_percent = round(
            (total_exposure / balance) * 100,
            2
        ) if balance else 0


        if exposure_percent > risk_limit:
            health = "OVEREXPOSED"

        elif exposure_percent > risk_limit * 0.7:
            health = "CAUTION"

        else:
            health = "HEALTHY"


        return {
            "balance": balance,
            "total_exposure": total_exposure,
            "exposure_percent": exposure_percent,
            "active_positions": active_positions,
            "allocation": allocation,
            "portfolio_health": health,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


portfolio_manager = PortfolioManager()
