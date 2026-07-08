from src.dashboard.dashboard_service import dashboard


class DashboardAPI:

    def get_status(self):
        return dashboard.status()

    def get_performance(self):
        return dashboard.get_performance()

    def get_alerts(self):
        return dashboard.get_alerts()

    def get_health(self):
        status = dashboard.status()

        return {
            "system": status.get("system"),
            "pipeline": status.get("pipeline"),
            "engine_health": status.get("engine_health")
        }


dashboard_api = DashboardAPI()
