from src.execution.execution_state import ExecutionState
from src.execution.failover_manager import FailoverManager
from src.execution.recovery_manager import RecoveryManager


def test_failover_recovery():

    state = ExecutionState(
        "test_execution_state.json"
    )

    failover = FailoverManager(
        state
    )

    recovery = RecoveryManager(
        state
    )

    data = {
        "order_id": "123",
        "status": "PENDING"
    }

    assert failover.trigger_failover(data)

    assert failover.is_failed()

    restored = recovery.restore()

    assert restored["order_id"] == "123"
    assert restored["status"] == "PENDING"

    recovery.clear_recovery()


if __name__ == "__main__":
    test_failover_recovery()
    print("V3.32.3 Failover Recovery Test Passed")
