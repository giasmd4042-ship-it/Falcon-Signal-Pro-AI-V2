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
    def get_account_summary(self):

        performance = self.get_performance()

        return {
            "balance": 10000,
            "equity": 10500,
            "free_margin": 9800,
            "used_margin": 200,
            "margin_level": "5250%",
            "unrealized_pnl": performance.get(
                "total_profit",
                0
            )
        }
    def get_risk_level(self):

        risk_snapshot = self.get_risk_snapshot()

        exposure = risk_snapshot.get(
            "exposure",
            0
        )

        risk_score = min(
            exposure,
            100
        )

        if risk_score >= 80:
            level = "HIGH"

        elif risk_score >= 40:
            level = "MEDIUM"

        else:
            level = "LOW"

        return {
            "risk_level": level,
            "exposure": exposure,
            "risk_score": risk_score,
            "risk_status": "SAFE" if risk_score < 40 else "WARNING"
        }
        
    def get_performance(self):

        return dashboard_state.snapshot().get(
            "performance",
            {}
        )    

    def get_intelligence(self):

        performance = self.get_performance()

        return {
            "best_strategy": performance.get(
                "best_strategy",
                "UNKNOWN"
            ),

            "win_rate": performance.get(
                "win_rate",
                0
            ),

            "total_profit": performance.get(
      
          "total_profit",
                0
            ),

            "average_win": performance.get(
                "average_win",
                0
            ),

            "average_loss": performance.get(
                "average_loss",
                0
            ),

            "profit_factor": performance.get(
                "profit_factor",
                0
            ),
            "max_drawdown": performance.get(
                "max_drawdown",
                0
            ),

            "recovery_factor": performance.get(
                "recovery_factor",
                0
            ),

            "average_return": performance.get(
                "average_return",
                0
            ),
            "market_regime": list(
                performance.get(
                    "regimes",
                    {}
                ).keys()
            )
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



    def get_persisted_metrics(self):

        try:
            from src.dashboard.metrics_store import metrics_store

            return metrics_store.load()

        except Exception:
            return {}


dashboard_api = DashboardAPI()
