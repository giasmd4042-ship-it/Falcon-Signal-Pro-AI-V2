from datetime import datetime
import json
import os


class TradeAuditLogger:

    def __init__(self, file_path="logs/trade_audit.json"):

        self.file_path = file_path
        self.events = []

        self.load()


    def load(self):

        if os.path.exists(self.file_path):

            with open(self.file_path, "r") as file:
                self.events = json.load(file)


    def record(
        self,
        symbol,
        side,
        quantity,
        status
    ):

        event = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity,
            "status": status,
            "timestamp": datetime.now(datetime.UTC).isoformat()
        }

        self.events.append(event)

        with open(self.file_path, "w") as file:
            json.dump(
                self.events,
                file,
                indent=4
            )

        return event


    def history(self):

        return self.events


trade_audit_logger = TradeAuditLogger()
