from src.core.config import ENABLE_LIVE_TRADING, BROKER_MODE, DATA_MODE
from src.security.api_key_manager import api_key_manager
from src.security.safety_guard import safety_guard


class LiveSafetyValidator:


    def validate(self):

        keys = api_key_manager.validate_keys()


        checks = {

            "live_enabled":
                ENABLE_LIVE_TRADING,

            "broker_live_mode":
                BROKER_MODE == "live",

            "data_live_mode":
                DATA_MODE == "live",

            "api_keys":
                keys["valid"],

            "safety_guard":
                safety_guard.allow_trade()

        }


        return {

            "status":
                "READY" if all(checks.values()) else "BLOCKED",

            "checks":
                checks,

            "engine":
                "V3.36"

        }



live_safety_validator = LiveSafetyValidator()
