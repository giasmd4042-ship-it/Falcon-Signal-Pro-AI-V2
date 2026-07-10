from datetime import datetime, timezone


class DashboardState:

    def __init__(self):

        self.signal = None
        self.positions = []
        self.orders = []
        self.performance = {}
        self.alerts = []


    def update(self, result):

        self.signal = result.get("signal")

        self.positions = [
            {
                "symbol": p.symbol,
                "quantity": p.quantity,
                "entry_price": p.entry_price,
                "side": p.side
            }
            for p in result.get("position", [])
        ]


        order = result.get("order")

        self.orders = []

        if order:

            self.orders.append(
                {
                    "symbol": order.symbol,
                    "side": order.side.value,
                    "quantity": order.quantity,
                    "order_type": order.order_type.value,
                    "status": order.status.value,
                    "filled_quantity": order.filled_quantity
                }
            )


        self.performance = result.get(
            "analytics",
            {}
        )


        return True



    def snapshot(self):

        return {

            "signal": self.signal,

            "positions": self.positions,

            "orders": self.orders,

            "performance": self.performance,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }



dashboard_state = DashboardState()
