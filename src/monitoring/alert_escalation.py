from datetime import datetime


class AlertEscalation:

    def __init__(self):

        self.alerts = []


    def send(
        self,
        level,
        message,
        data=None
    ):

        alert = {
            "level": level,
            "message": message,
            "data": data,
            "timestamp": datetime.now(datetime.UTC).isoformat()
        }

        self.alerts.append(alert)

        return alert


    def get_alerts(self):

        return self.alerts


    def critical_count(self):

        return len(
            [
                alert
                for alert in self.alerts
                if alert["level"] == "CRITICAL"
            ]
        )


alert_escalation = AlertEscalation()
