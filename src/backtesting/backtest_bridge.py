from datetime import datetime

from src.backtesting.backtest_analyzer import backtest_analyzer
from src.backtesting.risk_analytics import risk_analytics
from src.backtesting.strategy_benchmark import strategy_benchmark
from src.backtesting.report_generator import backtest_report_generator


class BacktestBridge:
    """
    Falcon Signal Pro AI V3.30.0
    Backtesting Intelligence Bridge
    """

    def __init__(self):
        self.version = "V3.30.0"


    def analyze(self, data):

        backtest = data.get(
            "backtest",
            {}
        )

        equity = data.get(
            "equity_curve",
            []
        )

        strategies = data.get(
            "strategies",
            []
        )


        intelligence = backtest_analyzer.analyze(
            backtest
        )


        risk = risk_analytics.analyze(
            equity
        )


        benchmark = strategy_benchmark.rank(
            strategies
        )


        report = backtest_report_generator.generate(
            backtest,
            risk,
            benchmark
        )


        return {
            "intelligence": intelligence,
            "risk": risk,
            "benchmark": benchmark,
            "report": report,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


backtest_bridge = BacktestBridge()
