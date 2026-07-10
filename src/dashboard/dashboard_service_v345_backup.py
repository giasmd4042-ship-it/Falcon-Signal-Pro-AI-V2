from datetime import datetime, timezone
import json
from pathlib import Path

try:
    from src.monitoring.alert_manager import alert_manager
except Exception:
    alert_manager = None


STATE_FILE = Path("dashboard_state.json")


class DashboardService:


    def update(self, result):

        data = {
            "signal": result.get("signal"),
            "positions": result.get("position", []),
            "orders": [
                result.get("order")
            ] if result.get("order") else [],
            "performance": result.get("analytics", {})
        }

        STATE_FILE.write_text(
            json.dumps(
                data,
                default=str,
                indent=4
            ),
            encoding="utf-8"
        )


    def load_state(self):

        if not STATE_FILE.exists():

            return {
                "signal": None,
                "positions": [],
                "orders": [],
                "performance": {}
            }

        try:

            return json.loads(
                STATE_FILE.read_text(
                    encoding="utf-8"
                )
            )

        except Exception:

            return {
                "signal": None,
                "positions": [],
                "orders": [],
                "performance": {}
            }



    def status(self):

        data = self.load_state()

        return {

            "system": "ONLINE",

            "pipeline": "RUNNING",

            "signal": data.get("signal"),

            "positions": data.get("positions", []),

            "orders": data.get("orders", []),

            "performance": data.get("performance", {}),

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

            "engine": "V3.44"

        }



    def get_positions(self):

        return self.load_state().get(
            "positions",
            []
        )


    def get_orders(self):

        return self.load_state().get(
            "orders",
            []
        )


    def get_performance(self):

        return self.load_state().get(
            "performance",
            {}
        )



    def get_alerts(self):

        try:

            if alert_manager:
                return alert_manager.get_alerts()

        except Exception:
            pass

        return []



dashboard = DashboardService()
