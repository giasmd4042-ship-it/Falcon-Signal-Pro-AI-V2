from datetime import datetime


class BacktestReportGenerator:
    """
    Falcon Signal Pro AI V3.29.3
    AI Backtest Report Generator
    """

    def __init__(self):
        self.version = "V3.29.3"

    def generate(
        self,
        backtest,
        risk,
        benchmark
    ):

        report = {
            "summary": {
                "net_profit": backtest.get("net_profit", 0),
                "win_rate": backtest.get("win_rate", 0),
                "trades": backtest.get("trades", 0),
            },
            "risk": risk,
            "benchmark": benchmark,
            "recommendation": self._recommend(
                backtest,
                risk
            ),
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }

        return report

    def _recommend(
        self,
        backtest,
        risk
    ):

        win_rate = backtest.get("win_rate", 0)
        risk_score = risk.get("risk_score", 0)

        if win_rate >= 70 and risk_score >= 90:
            return "READY_FOR_LIVE"

        if win_rate >= 60:
            return "PAPER_TRADE"

        return "NEEDS_OPTIMIZATION"


backtest_report_generator = BacktestReportGenerator()
