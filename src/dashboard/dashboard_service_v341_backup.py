from datetime import datetime, timezone

try:
    from src.monitoring.alert_manager import alert_manager
except Exception:
    alert_manager = None


class DashboardService:

    def __init__(self):
        self._latest_result = {
            "positions": [],
            "orders": [],
            "performance": {},
            "signal": None
        }


    def update(self, result):

        self._latest_result = {
            "signal": result.get("signal"),
            "positions": result.get("position", []),
            "orders": [result.get("order")] if result.get("order") else [],
            "performance": result.get("analytics", {})
        }


    def status(self):

        return {
            "system": "ONLINE",
            "pipeline": "RUNNING",
            "signal": self._latest_result.get("signal"),
            "positions": self.get_positions(),
            "orders": self.get_orders(),
            "alerts": self.get_alerts(),
            "performance": self.get_performance(),

            "engine_health": {
                "signal_engine": "OK",
                "risk_guard": "OK",
                "execution": "OK",
                "analytics": "OK",
                "dashboard": "OK"
            },

            "timestamp": datetime.now(timezone.utc).isoformat(),
            "engine": "V3.38"
        }


    def get_positions(self):
        return self._latest_result.get("positions", [])


    def get_orders(self):
        return self._latest_result.get("orders", [])


    def get_alerts(self):

        try:
            if alert_manager:
                return alert_manager.get_alerts()
        except Exception:
            pass

        return []


    def get_performance(self):
        return self._latest_result.get("performance", {})



dashboard = DashboardService()

