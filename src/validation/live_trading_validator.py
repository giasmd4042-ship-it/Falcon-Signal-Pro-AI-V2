from src.core.config import ENABLE_LIVE_TRADING, BROKER_MODE
from src.security.api_key_manager import api_key_manager
from src.security.safety_guard import safety_guard


class LiveTradingValidator:


    def validate(self):

        checks = {

            "live_enabled":
                ENABLE_LIVE_TRADING,

            "broker_mode":
                BROKER_MODE == "live",

            "api_key":
                api_key_manager.has_key("BROKER_API_KEY"),

            "safety":
                safety_guard.allow_trade()

        }


        return {
            "status": "READY" if all(checks.values()) else "BLOCKED",
            "checks": checks,
            "engine": "V3.35"
        }



live_trading_validator = LiveTradingValidator()
