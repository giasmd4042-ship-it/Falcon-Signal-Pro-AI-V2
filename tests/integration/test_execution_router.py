from src.execution.execution_router import ExecutionRouter
from src.brokers.mt5_broker import mt5_broker


router = ExecutionRouter()

assert mt5_broker.connect()

router.register_broker("mt5", mt5_broker)

result = router.place_order(
    "mt5",
    {
        "symbol": "EURUSDm",
        "volume": 0.01,
    },
)

print(result)

assert result["success"] is True

positions = mt5_broker.get_positions()

assert len(positions) > 0

print("Execution Router Test Passed")

mt5_broker.disconnect()
