from config.settings import (
    ENVIRONMENT,
    MODE,
    RISK_SETTINGS
)


class ConfigValidator:


    def validate_environment(self):

        allowed = [
            "development",
            "production",
            "testing"
        ]

        return ENVIRONMENT in allowed


    def validate_mode(self):

        allowed = [
            "paper",
            "live"
        ]

        return MODE in allowed


    def validate_risk(self):

        return (
            RISK_SETTINGS["max_position_size"] > 0
            and
            RISK_SETTINGS["max_daily_loss"] > 0
        )


    def validate_all(self):

        return {
            "environment": self.validate_environment(),
            "mode": self.validate_mode(),
            "risk": self.validate_risk()
        }


config_validator = ConfigValidator()
