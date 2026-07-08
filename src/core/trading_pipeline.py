from src.data.paper_market_data import PaperMarketData
from src.signals.trend_following import TrendFollowingSignal

from src.execution.paper_broker import PaperBroker
from src.execution.order_execution_engine import OrderExecutionEngine
from src.execution.order import Order, OrderSide, OrderType

from src.execution.execution_risk_guard import ExecutionRiskGuard
from src.execution.position_manager import PositionManager, Position

from src.portfolio.performance_analytics import performance_analytics

from src.monitoring.system_logger import system_logger
from src.monitoring.alert_manager import alert_manager



class TradingPipeline:


    def __init__(self):

        self.market = PaperMarketData()
        self.signal = TrendFollowingSignal()

        self.broker = PaperBroker()
        self.engine = OrderExecutionEngine(self.broker)

        self.risk = ExecutionRiskGuard()

        self.positions = PositionManager()


        system_logger.log("PIPELINE_INITIALIZED")

        alert_manager.send(
            "INFO",
            "Trading Pipeline Initialized"
        )



    def run(self):

        system_logger.log("PIPELINE_START")


        alert_manager.send(
            "INFO",
            "Pipeline Started"
        )


        self.market.connect()


        signal = self.signal.generate(
            self.market
        )


        system_logger.log(
            "SIGNAL_GENERATED",
            signal
        )


        alert_manager.send(
            "SIGNAL",
            "Signal Generated",
            signal
        )


        if signal["signal"] == "BUY":


            approved = self.risk.approve(
                1,
                10000,
                100
            )


            system_logger.log(
                "RISK_CHECK",
                {"approved": approved}
            )


            if not approved:

                alert_manager.send(
                    "WARNING",
                    "Risk Check Failed"
                )

                return {
                    "signal": signal,
                    "order": "BLOCKED"
                }



            order = Order(
                signal["symbol"],
                OrderSide.BUY,
                1,
                OrderType.MARKET
            )


            result = self.engine.execute(order)


            system_logger.log(
                "ORDER_EXECUTED",
                {
                    "status": result.status.value,
                    "symbol": result.symbol
                }
            )


            alert_manager.send(
                "TRADE",
                "Order Executed",
                {
                    "symbol": result.symbol,
                    "status": result.status.value
                }
            )



            position = Position(
                signal["symbol"],
                1,
                self.market.get_price(signal["symbol"]),
                "LONG"
            )


            self.positions.add_position(position)


            system_logger.log(
                "POSITION_UPDATED",
                {
                    "symbol": signal["symbol"]
                }
            )


            analytics = performance_analytics.analyze()


            alert_manager.send(
                "SUCCESS",
                "Pipeline Completed",
                analytics
            )


            return {
                "signal": signal,
                "order": result.status.value,
                "position": self.positions.get_all_positions(),
                "analytics": analytics
            }



        return {
            "signal": signal,
            "order": "NONE"
        }



pipeline = TradingPipeline()
