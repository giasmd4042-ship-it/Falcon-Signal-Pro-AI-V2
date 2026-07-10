from src.dashboard.dashboard_state import dashboard_state


class DashboardAPI:


    def get_health(self):

        return {
            "system": "ONLINE",
            "pipeline": "RUNNING",

            "engine_health": {
                "signal_engine": "OK",
                "risk_guard": "OK",
                "execution": "OK",
                "analytics": "OK",
                "dashboard": "OK"
            }
        }



    def get_signal(self):

        return dashboard_state.snapshot().get(
            "signal"
        )



    def get_positions(self):

        return dashboard_state.snapshot().get(
            "positions",
            []
        )



    def get_orders(self):

        return dashboard_state.snapshot().get(
            "orders",
            []
        )



    def get_performance(self):

        return dashboard_state.snapshot().get(
            "performance",
            {}
        )



    def get_signal_history(self):

        return dashboard_state.snapshot().get(
            "signal_history",
            []
        )



    def get_trade_history(self):

        return dashboard_state.snapshot().get(
            "trade_history",
            []
        )



    def get_risk_snapshot(self):

        return dashboard_state.snapshot().get(
            "risk_snapshot",
            {}
        )



dashboard_api = DashboardAPI()