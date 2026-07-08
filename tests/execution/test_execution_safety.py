from src.execution.order import Order, OrderSide
from src.execution.execution_validator import ExecutionValidator
from src.execution.execution_risk_guard import ExecutionRiskGuard
from src.execution.duplicate_order_checker import DuplicateOrderChecker


def test_execution_safety():

    order = Order(
        symbol="BTCUSDT",
        side=OrderSide.BUY,
        quantity=0.5
    )

    validator = ExecutionValidator()
    guard = ExecutionRiskGuard()
    checker = DuplicateOrderChecker()

    assert validator.validate(order)

    assert guard.approve(
        quantity=0.5,
        balance=10000,
        required=100
    )

    assert checker.is_duplicate(order) is False

    checker.add_order(order)

    assert checker.is_duplicate(order)


if __name__ == "__main__":
    test_execution_safety()
    print("V3.32.2 Execution Safety Test Passed")
