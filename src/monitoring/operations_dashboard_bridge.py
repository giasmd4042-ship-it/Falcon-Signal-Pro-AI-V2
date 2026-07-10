from datetime import datetime

from src.monitoring.health_monitor import health_monitor
from src.monitoring.execution_metrics import execution_metrics
from src.monitoring.alert_escalation import alert_escalation


class OperationsDashboardBridge:

    def __init__(self):
        self.version = "V3.35.5"


    def get_status(self):

        return {
            "version": self.version,
            "health": health_monitor.check(),
            "metrics": execution_metrics.report(),
            "alerts": {
                "total": len(alert_escalation.get_alerts()),
                "critical": alert_escalation.critical_count()
            },
            "timestamp": datetime.utcnow().isoformat()
        }


operations_dashboard_bridge = OperationsDashboardBridge()
