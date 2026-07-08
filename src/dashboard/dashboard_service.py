from datetime import datetime

try:
    from src.monitoring.alert_manager import alert_manager
except Exception:
    alert_manager = None

try:
    from src.portfolio.performance_analytics import performance_analytics
except Exception:
    performance_analytics = None


class DashboardService:

    def status(self):
        return {
            "system": "ONLINE",
            "pipeline": "RUNNING",
            "positions": self.get_positions(),
            "orders": self.get_orders(),
            "alerts": self.get_alerts(),
            "performance": self.get_performance(),
            "engine_health": {
                "signal_engine": "OK",
                "risk_guard": "OK",
                "execution": "OK",
                "analytics": "OK"
            },
            "timestamp": datetime.utcnow().isoformat(),
            "engine": "V3.33"
        }

    def get_positions(self):
        return []

    def get_orders(self):
        return []

    def get_alerts(self):
        try:
            if alert_manager:
                return alert_manager.get_alerts()
        except Exception:
            pass
        return []

    def get_performance(self):
        try:
            if performance_analytics:
                return performance_analytics.analyze()
        except Exception:
            pass
        return {}


dashboard = DashboardService()
