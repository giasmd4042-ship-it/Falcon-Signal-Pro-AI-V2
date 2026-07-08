class ConfidenceLearning:
    """
    Falcon Signal Pro AI V3.25.4
    Historical confidence adjustment engine
    """

    def __init__(self):
        self.version = "V3.25.4"


    def adjust(self, confidence, statistics):

        if not statistics:
            return confidence

        win_rate = statistics.get(
            "win_rate",
            0
        )

        adjustment = 0

        if win_rate >= 80:
            adjustment = 10

        elif win_rate >= 60:
            adjustment = 5

        elif win_rate < 40:
            adjustment = -10


        new_confidence = confidence + adjustment

        if new_confidence > 100:
            new_confidence = 100

        if new_confidence < 0:
            new_confidence = 0


        return {
            "original_confidence": confidence,
            "adjusted_confidence": new_confidence,
            "adjustment": adjustment,
            "historical_win_rate": win_rate,
            "engine": self.version
        }


confidence_learning = ConfidenceLearning()
