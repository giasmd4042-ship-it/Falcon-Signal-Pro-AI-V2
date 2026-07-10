from datetime import datetime

try:
    from src.portfolio.performance_analytics import performance_analytics
except Exception:
    performance_analytics = None

try:
    from src.monitoring.alert_manager import alert_manager
except Exception:
    alert_manager = None


class MetricsCollector:

    def collect(self):
        performance = self.get_performance()

        return {
            "uptime": "ACTIVE",
            "trades": performance.get("total_trades", 0),
            "wins": performance.get("wins", 0),
            "profit": performance.get("total_profit", 0),
            "alerts": self.get_alert_count(),
            "health": "OK",
            "timestamp": datetime.now(datetime.UTC).isoformat(),
            "engine": "V3.33"
        }

    def get_performance(self):
        try:
            if performance_analytics:
                return performance_analytics.analyze()
        except Exception:
            pass

        return {}

    def get_alert_count(self):
        try:
            if alert_manager:
                return len(alert_manager.get_alerts())
        except Exception:
            pass

        return 0


metrics = MetricsCollector()
