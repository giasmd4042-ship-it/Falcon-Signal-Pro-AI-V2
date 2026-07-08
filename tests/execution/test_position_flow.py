from src.execution.paper_broker import PaperBroker
from src.execution.order import Order, OrderSide
from src.execution.order_execution_engine import OrderExecutionEngine
from src.execution.position_manager import PositionManager
from src.execution.trade_synchronizer import TradeSynchronizer
from src.execution.live_position_monitor import LivePositionMonitor


def test_position_flow():

    broker = PaperBroker()

    engine = OrderExecutionEngine(
        broker
    )

    order = Order(
        symbol="BTCUSDT",
        side=OrderSide.BUY,
        quantity=0.5
    )

    engine.execute(order)

    position_manager = PositionManager()

    synchronizer = TradeSynchronizer(
        broker,
        position_manager
    )

    synchronizer.synchronize()

    monitor = LivePositionMonitor(
        position_manager
    )

    snapshot = monitor.get_positions_snapshot()

    assert len(snapshot) == 1
    assert snapshot[0]["symbol"] == "BTCUSDT"


if __name__ == "__main__":
    test_position_flow()
    print("V3.32.1 Position Flow Test Passed")
