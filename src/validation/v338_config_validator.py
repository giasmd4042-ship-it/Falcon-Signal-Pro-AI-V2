from src.security.production_environment import production_environment
from src.core.config import DATA_MODE, BROKER_MODE, ENABLE_LIVE_TRADING


class ProductionConfigValidator:


    def validate(self):

        checks = {

            "production_environment":
                production_environment.is_production(),

            "live_enabled":
                ENABLE_LIVE_TRADING,

            "data_mode":
                DATA_MODE == "live",

            "broker_mode":
                BROKER_MODE == "live"

        }


        return {

            "status":
                "READY" if all(checks.values()) else "BLOCKED",

            "checks":
                checks,

            "engine":
                "V3.38"

        }



production_config_validator = ProductionConfigValidator()
