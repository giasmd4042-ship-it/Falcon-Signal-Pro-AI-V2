from datetime import datetime


class MarketMemory:
    """
    Falcon Signal Pro AI V3.25
    Market memory intelligence layer
    """

    def __init__(self):
        self.history = []
        self.version = "V3.25.0"

    def store(self, market_state):
        record = {
            "timestamp": datetime.now().isoformat(),
            "data": market_state
        }

        self.history.append(record)
        return record

    def recall(self):
        return self.history

    def last_state(self):
        if self.history:
            return self.history[-1]

        return None


market_memory = MarketMemory()
