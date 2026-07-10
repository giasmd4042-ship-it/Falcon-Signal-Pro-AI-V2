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

        return dashboard_state.signal


    def get_signal_history(self):

        return dashboard_state.signal_history


    def get_trade_history(self):

        return dashboard_state.trade_history


    def get_risk_snapshot(self):

        return dashboard_state.risk_snapshot


    def get_performance(self):

        return dashboard_state.performance


    def get_intelligence(self):

        performance = dashboard_state.performance

        return {
            "best_strategy": performance.get(
                "best_strategy"
            ),
            "win_rate": performance.get(
                "win_rate",
                0
            ),
            "total_profit": performance.get(
                "total_profit",
                0
            ),
            "market_regime": list(
                performance.get(
                    "regimes",
                    {}
                ).keys()
            ),
            "strategy_count": len(
                performance.get(
                    "strategies",
                    {}
                )
            )
        }


dashboard_api = DashboardAPI()
