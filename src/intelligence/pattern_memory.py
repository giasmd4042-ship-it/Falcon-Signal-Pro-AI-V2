from datetime import datetime


class PatternMemory:
    """
    Falcon Signal Pro AI V3.25
    Pattern recognition memory layer
    """

    def __init__(self):
        self.patterns = []
        self.version = "V3.25.0"

    def save_pattern(self, pattern_name, result, confidence=0):
        pattern = {
            "timestamp": datetime.now().isoformat(),
            "pattern": pattern_name,
            "result": result,
            "confidence": confidence
        }

        self.patterns.append(pattern)
        return pattern

    def find_patterns(self, pattern_name):
        return [
            item for item in self.patterns
            if item["pattern"] == pattern_name
        ]

    def all_patterns(self):
        return self.patterns


pattern_memory = PatternMemory()
