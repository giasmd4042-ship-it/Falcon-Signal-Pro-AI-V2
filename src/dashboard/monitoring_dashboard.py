from src.dashboard.dashboard_api import dashboard_api
from src.dashboard.metrics_collector import metrics


class MonitoringDashboard:

    def view(self):
        return {
            "status": dashboard_api.get_health(),
            "metrics": metrics.collect(),
            "performance": dashboard_api.get_performance(),
            "alerts": dashboard_api.get_alerts()
        }


monitoring_dashboard = MonitoringDashboard()
