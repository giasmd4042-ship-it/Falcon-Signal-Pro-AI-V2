from src.core.trading_config import config


class StartupValidator:

    def __init__(self):
        self.errors = []


    def validate_config(self):

        required = [
            "environment",
            "broker",
            "risk_enabled",
            "failover_enabled",
            "recovery_enabled"
        ]

        for item in required:
            if item not in config.data:
                self.errors.append(
                    f"Missing config: {item}"
                )

        return len(self.errors) == 0


    def validate_system(self):

        checks = [
            self.validate_config()
        ]

        return all(checks)


    def report(self):

        if self.errors:
            return {
                "status": "FAILED",
                "errors": self.errors
            }

        return {
            "status": "READY",
            "errors": []
        }


startup_validator = StartupValidator()
