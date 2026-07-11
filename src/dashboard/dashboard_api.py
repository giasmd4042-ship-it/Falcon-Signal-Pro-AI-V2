from src.dashboard.dashboard_state import dashboard_state
from src.execution.live_connection_manager import live_connection_manager

class DashboardAPI:


    def get_health(self):

        return {
            "system": "ONLINE",
            "pipeline": "RUNNING",
            "engine_health": {
                "execution": "OK",
                "dashboard": "OK",
                "analytics": "OK",
                "risk_guard": "OK"
            }
        }



    def get_signal(self):

        return dashboard_state.snapshot().get(
            "signal"
        )



    def get_risk_snapshot(self):

        return dashboard_state.snapshot().get(
            "risk_snapshot",
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



    def get_performance(self):

        return dashboard_state.snapshot().get(
            "performance",
            {}
        )



    def get_intelligence(self):

        performance = self.get_performance()

        return {
            "best_strategy":
                performance.get(
                    "best_strategy",
                    "UNKNOWN"
                ),

            "win_rate":
                performance.get(
                    "win_rate",
                    0
                ),

            "total_profit":
                performance.get(
                    "total_profit",
                    0
                ),

            "market_regime":
                list(
                    performance.get(
                        "regimes",
                        {}
                    ).keys()
                )
        }



    def get_monitoring(self):

        performance = self.get_performance()

        return {

            "portfolio": {

                "open_positions":
                    len(
                        dashboard_state.snapshot().get(
                            "positions",
                            []
                        )
                    ),

                "exposure":
                    dashboard_state.snapshot().get(
                        "risk_snapshot",
                        {}
                    ).get(
                        "exposure",
                        0
                    )

            },

            "performance": {

                "trades":
                    performance.get(
                        "total_trades",
                        0
                    ),

                "wins":
                    performance.get(
                        "wins",
                        0
                    ),

                "losses":
                    performance.get(
                        "losses",
                        0
                    ),

                "profit":
                    performance.get(
                        "total_profit",
                        0
                    )

            }

        }


    def get_broker_health(self):        
        connection = live_connection_manager.get_status()
        

        return {        
            "broker": "CONNECTED" if connection["connected"] else "DISCONNECTED",
            "authentication": "VERIFIED" if connection["error"] is None else "FAILED",
            "session": "ACTIVE" if connection["connected"] else "INACTIVE",
            "gateway": "ONLINE",
            "environment": "PAPER",
            "permission": "ALLOWED",
            "engine": connection["engine"],
        }


dashboard_api = DashboardAPI()
