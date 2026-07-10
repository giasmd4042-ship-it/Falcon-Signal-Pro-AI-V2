from datetime import datetime


class HealthMonitor:

    def __init__(self):
        self.status = "INITIALIZED"


    def check(
        self,
        broker=True,
        risk=True,
        failover=True
    ):

        checks = {
            "broker": broker,
            "risk": risk,
            "failover": failover
        }

        healthy = all(checks.values())

        self.status = (
            "HEALTHY"
            if healthy
            else "DEGRADED"
        )

        return {
            "status": self.status,
            "checks": checks,
            "timestamp": datetime.now(datetime.UTC).isoformat()
        }


health_monitor = HealthMonitor()
