from datetime import datetime, timezone
import json
from pathlib import Path

try:
    from src.monitoring.alert_manager import alert_manager
except Exception:
    alert_manager = None


STATE_FILE = Path("dashboard_state.json")


class DashboardService:


    def serialize_position(self, position):

        if isinstance(position, dict):
            return position

        return {
            "symbol": getattr(position, "symbol", None),
            "quantity": getattr(position, "quantity", 0),
            "entry_price": getattr(position, "entry_price", 0),
            "side": getattr(position, "side", None)
        }



    def serialize_order(self, order):

        if isinstance(order, dict):
            return order

        return {
            "symbol": getattr(order, "symbol", None),
            "side": getattr(
                getattr(order, "side", None),
                "value",
                None
            ),
            "quantity": getattr(order, "quantity", 0),
            "order_type": getattr(
                getattr(order, "order_type", None),
                "value",
                None
            ),
            "status": getattr(
                getattr(order, "status", None),
                "value",
                None
            ),
            "filled_quantity": getattr(
                order,
                "filled_quantity",
                0
            )
        }



    def update(self, result):

        data = {

            "signal": result.get("signal"),

            "positions": [
                self.serialize_position(p)
                for p in result.get(
                    "position",
                    []
                )
            ],

            "orders": [
                self.serialize_order(
                    result.get("order")
                )
            ]
            if result.get("order")
            else [],


            "performance": result.get(
                "analytics",
                {}
            )

        }


        STATE_FILE.write_text(
            json.dumps(
                data,
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


        return json.loads(
            STATE_FILE.read_text(
                encoding="utf-8"
            )
        )



    def status(self):

        data = self.load_state()

        return {

            "system": "ONLINE",

            "pipeline": "RUNNING",

            "signal": data.get(
                "signal"
            ),

            "positions": data.get(
                "positions",
                []
            ),

            "orders": data.get(
                "orders",
                []
            ),

            "performance": data.get(
                "performance",
                {}
            ),

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

            "engine": "V3.45"

        }



    def get_alerts(self):

        try:

            if alert_manager:
                return alert_manager.get_alerts()

        except Exception:
            pass

        return []



dashboard = DashboardService()
