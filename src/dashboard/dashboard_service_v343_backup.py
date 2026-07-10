from datetime import datetime, timezone

try:
    from src.monitoring.alert_manager import alert_manager
except Exception:
    alert_manager = None


LATEST_RESULT = {
    "signal": None,
    "positions": [],
    "orders": [],
    "performance": {}
}


class DashboardService:


    def update(self, result):

        global LATEST_RESULT

        LATEST_RESULT = {
            "signal": result.get("signal"),
            "positions": result.get("position", []),
            "orders": [
                result.get("order")
            ] if result.get("order") else [],
            "performance": result.get("analytics", {})
        }



    def status(self):

        global LATEST_RESULT

        return {
            "system": "ONLINE",
            "pipeline": "RUNNING",

            "signal": LATEST_RESULT["signal"],

            "positions": LATEST_RESULT["positions"],

            "orders": LATEST_RESULT["orders"],

            "performance": LATEST_RESULT["performance"],

            "alerts": self.get_alerts(),

            "engine_health": {
                "signal_engine": "OK",
                "risk_guard": "OK",
                "execution": "OK",
                "analytics": "OK",
                "dashboard": "OK"
            },

            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),

            "engine": "V3.42"
        }



    def get_positions(self):
        return LATEST_RESULT["positions"]


    def get_orders(self):
        return LATEST_RESULT["orders"]


    def get_performance(self):
        return LATEST_RESULT["performance"]



    def get_alerts(self):

        try:
            if alert_manager:
                return alert_manager.get_alerts()
        except Exception:
            pass

        return []



dashboard = DashboardService()
