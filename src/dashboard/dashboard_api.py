from src.dashboard.dashboard_state import dashboard_state


class DashboardAPI:

    def get_health(self):
        return {
            "system": "ONLINE",
            "pipeline": "RUNNING",
            "engine_health": {
                "execution": "OK",
                "dashboard": "OK",
                "analytics": "OK",
                "risk_guard": "OK",
            },
        }

    def get_signal(self):
        return dashboard_state.snapshot().get("signal")

    def get_risk_snapshot(self):
        return dashboard_state.snapshot().get("risk_snapshot", {})

    def get_signal_history(self):
        return dashboard_state.snapshot().get("signal_history", [])

    def get_trade_history(self):
        return dashboard_state.snapshot().get("trade_history", [])

    def get_performance(self):
        return dashboard_state.snapshot().get("performance", {})

    def get_intelligence(self):
        performance = self.get_performance()

        return {
            "best_strategy": performance.get("best_strategy", "UNKNOWN"),
            "win_rate": performance.get("win_rate", 0),
            "total_profit": performance.get("total_profit", 0),
            "market_regime": list(performance.get("regimes", {}).keys()),
        }

    def get_monitoring(self):
        performance = self.get_performance()

        return {
            "portfolio": {
                "open_positions": len(
                    dashboard_state.snapshot().get("positions", [])
                ),
                "exposure": dashboard_state.snapshot()
                .get("risk_snapshot", {})
                .get("exposure", 0),
            },
            "performance": {
                "trades": performance.get("total_trades", 0),
                "wins": performance.get("wins", 0),
                "losses": performance.get("losses", 0),
                "profit": performance.get("total_profit", 0),
            },
        }

    def get_risk_analytics(self):
        snapshot = dashboard_state.snapshot()
        risk = snapshot.get("risk_snapshot", {})
        performance = snapshot.get("performance", {})

        return {
            "status": risk.get("status", "UNKNOWN"),
            "exposure": risk.get("exposure", 0),
            "open_positions": risk.get("open_positions", 0),
            "total_trades": performance.get("total_trades", 0),
            "win_rate": performance.get("win_rate", 0),
            "profit": performance.get("total_profit", 0),
        }


dashboard_api = DashboardAPI()