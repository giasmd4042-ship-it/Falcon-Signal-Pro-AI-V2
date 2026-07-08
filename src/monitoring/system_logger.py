from datetime import datetime


class SystemLogger:


    def __init__(self):

        self.logs = []


    def log(self, event, data=None):

        entry = {
            "time": datetime.now().isoformat(),
            "event": event,
            "data": data
        }

        self.logs.append(entry)

        return entry


    def get_logs(self):

        return self.logs



system_logger = SystemLogger()
