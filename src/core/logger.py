from datetime import datetime


class SystemLogger:

    def __init__(self):
        self.events = []

    def log(self, level, message):
        event = {
            "level": level,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(event)
        return event

    def info(self, message):
        return self.log("INFO", message)

    def error(self, message):
        return self.log("ERROR", message)

    def warning(self, message):
        return self.log("WARNING", message)

    def get_logs(self):
        return self.events


logger = SystemLogger()
