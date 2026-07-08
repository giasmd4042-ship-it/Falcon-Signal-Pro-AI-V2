import json
import os
from datetime import datetime


class MemoryStorage:
    """
    Falcon Signal Pro AI V3.25.2
    Persistent intelligence memory storage
    """

    def __init__(self):
        self.file = "data/intelligence_memory.json"
        self.version = "V3.25.2"

        folder = os.path.dirname(self.file)

        if not os.path.exists(folder):
            os.makedirs(folder)

    def save(self, data):

        history = self.load()

        record = {
            "timestamp": datetime.now().isoformat(),
            "data": data
        }

        history.append(record)

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)

        return record

    def load(self):

        if not os.path.exists(self.file):
            return []

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_history(self):

        return self.load()


    def latest(self):

        history = self.load()

        if history:
            return history[-1]

        return None


memory_storage = MemoryStorage()

