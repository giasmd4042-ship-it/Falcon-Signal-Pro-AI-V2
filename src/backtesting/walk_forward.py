from datetime import datetime


class WalkForwardValidator:
    """
    Falcon Signal Pro AI V3.28.1
    Walk Forward Validation Engine
    """

    def __init__(self):
        self.version = "V3.28.1"

    def validate(self, train_results, test_results):

        train_win_rate = train_results.get("win_rate", 0)
        test_win_rate = test_results.get("win_rate", 0)

        stability = round(
            100 - abs(train_win_rate - test_win_rate),
            2
        )

        passed = (
            train_win_rate >= 55
            and test_win_rate >= 55
            and stability >= 80
        )

        return {
            "train_win_rate": train_win_rate,
            "test_win_rate": test_win_rate,
            "stability_score": stability,
            "passed": passed,
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


walk_forward_validator = WalkForwardValidator()
