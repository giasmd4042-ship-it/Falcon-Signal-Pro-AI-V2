from src.core.config import DATA_MODE, BROKER_MODE
from src.data.data_factory import data_factory
from src.execution.broker_factory import broker_factory
from src.security.safety_guard import safety_guard


class V335Validator:


    def validate(self):

        data_provider = data_factory.create()
        broker_provider = broker_factory.create()

        checks = {

            "data_factory":
                data_provider is not None,

            "broker_factory":
                broker_provider is not None,

            "data_mode":
                DATA_MODE in ["paper", "live"],

            "broker_mode":
                BROKER_MODE in ["paper", "live"],

            "safety_guard":
                safety_guard.allow_trade()

        }


        return {

            "status": "PASS" if all(checks.values()) else "FAIL",

            "checks": checks,

            "data_provider":
                type(data_provider).__name__,

            "broker_provider":
                type(broker_provider).__name__,

            "engine":
                "V3.35"

        }



v335_validator = V335Validator()
