from src.execution.order import Order, OrderSide
from src.execution.paper_broker import PaperBroker
from src.execution.order_execution_engine import OrderExecutionEngine
from src.execution.execution_bridge import ExecutionBridge


class TestSignal:

    def to_order(self):
        return Order(
            symbol="BTCUSDT",
            side=OrderSide.BUY,
            quantity=0.1
        )


def test_execution_flow():

    broker = PaperBroker()

    engine = OrderExecutionEngine(
        broker
    )

    bridge = ExecutionBridge(
        engine
    )

    result = bridge.submit_signal(
        TestSignal()
    )

    assert result.status.value == "FILLED"
    assert result.symbol == "BTCUSDT"
    assert result.filled_quantity == 0.1


if __name__ == "__main__":
    test_execution_flow()
    print("V3.32.0 Execution Flow Test Passed")
