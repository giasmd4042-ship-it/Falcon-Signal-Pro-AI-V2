from datetime import datetime, timezone


class DashboardState:

    def __init__(self):

        self.signal = None
        self.positions = []
        self.orders = []
        self.performance = {}
        self.alerts = []

        self.signal_history = []
        self.trade_history = []

        self.risk_snapshot = {
            "status": "SAFE",
            "exposure": 0,
            "open_positions": 0
        }



    def update(self, result):

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()


        self.signal = result.get(
            "signal"
        )


        if self.signal:

            self.signal_history.append(
                {
                    "time": timestamp,
                    "symbol": self.signal.get("symbol"),
                    "signal": self.signal.get("signal"),
                    "strategy": self.signal.get("strategy")
                }
            )


        self.positions = [

            {
                "symbol": p.symbol,
                "quantity": p.quantity,
                "entry_price": p.entry_price,
                "side": p.side
            }

            for p in result.get(
                "position",
                []
            )

        ]


        order = result.get(
            "order"
        )


        self.orders = []


        if order:

            trade = {

                "time": timestamp,
                "symbol": order.symbol,
                "side": order.side.value,
                "quantity": order.quantity,
                "order_type": order.order_type.value,
                "status": order.status.value,
                "filled_quantity": order.filled_quantity

            }


            self.orders.append(
                trade
            )

            self.trade_history.append(
                trade
            )



        self.performance = result.get(
            "analytics",
            {}
        )


        self.risk_snapshot = {

            "status": "SAFE",

            "exposure": len(
                self.positions
            ),

            "open_positions": len(
                self.positions
            )

        }


        return True



    def snapshot(self):

        return {

            "signal": self.signal,

            "positions": self.positions,

            "orders": self.orders,

            "performance": self.performance,

            "signal_history": self.signal_history,

            "trade_history": self.trade_history,

            "risk_snapshot": self.risk_snapshot,

            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()

        }



dashboard_state = DashboardState()