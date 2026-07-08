from datetime import datetime

from src.intelligence.memory_storage import memory_storage


class PatternMemory:
    """
    Falcon Signal Pro AI V3.25.2
    Persistent pattern recognition memory layer
    """

    def __init__(self):
        self.version = "V3.25.2"

    def save_pattern(self, pattern_name, result, confidence=0):

        pattern = {
            "timestamp": datetime.now().isoformat(),
            "pattern": pattern_name,
            "result": result,
            "confidence": confidence
        }

        memory_storage.save({
            "type": "pattern",
            "pattern": pattern
        })

        return pattern

    def find_patterns(self, pattern_name):

        history = memory_storage.load()

        return [
            item["data"]["pattern"]
            for item in history
            if item.get("data", {}).get("type") == "pattern"
            and item["data"]["pattern"].get("pattern") == pattern_name
        ]

    def all_patterns(self):

        history = memory_storage.load()

        return [
            item["data"]["pattern"]
            for item in history
            if item.get("data", {}).get("type") == "pattern"
        ]


pattern_memory = PatternMemory()
