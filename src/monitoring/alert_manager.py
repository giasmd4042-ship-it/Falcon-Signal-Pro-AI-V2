from datetime import datetime


class AlertManager:


    def __init__(self):

        self.alerts = []


    def send(self, level, message, data=None):

        alert = {
            "time": datetime.now().isoformat(),
            "level": level,
            "message": message,
            "data": data
        }

        self.alerts.append(alert)

        return alert



    def get_alerts(self):

        return self.alerts



    def clear(self):

        self.alerts = []

        return True



alert_manager = AlertManager()
