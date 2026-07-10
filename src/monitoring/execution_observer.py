from datetime import datetime

from src.monitoring.execution_metrics import execution_metrics
from src.monitoring.trade_audit_logger import trade_audit_logger
from src.monitoring.alert_escalation import alert_escalation


class ExecutionObserver:

    def on_order_success(self, order):
        execution_metrics.record_success()

        trade_audit_logger.record(
            order.symbol,
            order.side.value if hasattr(order.side, "value") else order.side,
            order.quantity,
            "FILLED"
        )

        return {
            "status": "SUCCESS",
            "symbol": order.symbol,
            "timestamp": datetime.now(datetime.UTC).isoformat()
        }


    def on_order_failure(self, error):
        execution_metrics.record_failure()

        alert_escalation.send(
            "CRITICAL",
            "Execution Failure",
            {"error": str(error)}
        )

        return {
            "status": "FAILED",
            "error": str(error),
            "timestamp": datetime.now(datetime.UTC).isoformat()
        }


execution_observer = ExecutionObserver()
