from src.dashboard.monitoring_dashboard import monitoring_dashboard


class UIBinding:

    def render(self):
        data = monitoring_dashboard.view()

        return {
            "status_card": {
                "system": data["status"]["system"],
                "pipeline": data["status"]["pipeline"]
            },

            "status_bar": {
                "health": data["metrics"]["health"],
                "uptime": data["metrics"]["uptime"]
            },

            "risk_card": {
                "risk_guard": data["status"]["engine_health"]["risk_guard"]
            },

            "performance_card": {
                "trades": data["metrics"]["trades"],
                "wins": data["metrics"]["wins"],
                "profit": data["metrics"]["profit"]
            },

            "alert_panel": data["alerts"]
        }


ui_binding = UIBinding()
