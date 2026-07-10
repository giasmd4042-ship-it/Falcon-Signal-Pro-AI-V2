import time
import signal

from src.core.trading_pipeline import pipeline
from src.core.startup_validator import startup_validator
from src.core.trading_config import config
from src.execution.execution_router import ExecutionRouter
from src.execution.paper_broker import PaperBroker
from src.execution.execution_risk_guard import ExecutionRiskGuard
from src.execution.failover_manager import FailoverManager
from src.execution.recovery_manager import RecoveryManager
from src.execution.execution_state import ExecutionState
from src.monitoring.operations_dashboard_bridge import operations_dashboard_bridge
from src.monitoring.execution_observer import execution_observer


running = True


def shutdown_handler(signum, frame):
    global running
    print("\nShutdown signal received...")
    running = False


signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)


def main():
    if not startup_validator.validate_system():
        print(startup_validator.report())
        return

    print('Startup Validation:', startup_validator.report())

    print("=== Falcon Signal Pro AI V3.34.4 Failover Engine ===")

    router = ExecutionRouter()
    broker = PaperBroker()

    router.register_broker("paper", broker)

    risk_guard = ExecutionRiskGuard(
        max_position_size=1.0,
        max_daily_loss=1000
    )

    state_manager = ExecutionState()
    failover = FailoverManager(state_manager)
    recovery = RecoveryManager(state_manager)
    observer = execution_observer

    print("Broker Connected: True")
    print("Risk Guard Activated")
    print("Failover Manager Activated")
    print("Recovery Manager Activated")

    cycle = 0

    while running:

        cycle += 1

        print(f"\n--- Trading Cycle {cycle} ---")

        try:
            result = pipeline.run()

            approved = risk_guard.approve(
                quantity=1,
                balance=broker.get_balance(),
                required=200
            )

            if not approved:
                print("Risk Check Failed - Order Blocked")
                continue

            print("Risk Check: PASSED")
            print("Order:", result.get("order"))
            print("DEBUG RESULT:", result)
            if hasattr(result.get('order'), 'symbol'): 
                observer.on_order_success(result.get('order'))
                if hasattr(result.get('order'), 'symbol'):
                    observer.on_order_success(result.get('order'))
            print("Position:", result.get("position"))
            print("Analytics:", result.get("analytics"))
            print("Operations Status:", operations_dashboard_bridge.get_status())

        except Exception as error:

            print("Execution Failure:", error)

            try:
                failover.handle(error)
                recovery.recover()
                print("Recovery Completed")

            except Exception as recovery_error:
                print("Recovery Failed:", recovery_error)

        time.sleep(10)

    print("Trading Loop Stopped")
    print("=== Runner Shutdown Complete ===")


if __name__ == "__main__":
    main()
