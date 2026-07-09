from src.security.production_environment import production_environment
from src.security.api_key_manager import api_key_manager
from src.security.safety_guard import safety_guard
from src.core.config import DATA_MODE, BROKER_MODE, ENABLE_LIVE_TRADING


class LivePermissionGate:


    def validate(self):

        checks = {


            "production":
                production_environment.is_production(),


            "live_enabled":
                ENABLE_LIVE_TRADING,


            "data_live":
                DATA_MODE == "live",


            "broker_live":
                BROKER_MODE == "live",


            "api_keys":
                api_key_manager.validate_keys()["valid"],


            "safety":
                safety_guard.allow_trade()

        }



        return {


            "status":

                "ALLOW"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "engine":

                "V3.38"

        }




live_permission_gate = LivePermissionGate()
