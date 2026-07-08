from src.core.config import VERSION, DATA_MODE, BROKER_MODE

from src.data.data_factory import data_factory
from src.execution.broker_adapter import broker_adapter
from src.security.safety_guard import safety_guard
from src.security.environment import environment


class V334Validator:


    def validate(self):

        checks = {

            "version_configured":
                VERSION.startswith("3.34"),

            "data_factory":
                data_factory.create() is not None,

            "broker_adapter":
                broker_adapter is not None,

            "safety_guard":
                safety_guard.allow_trade(),

            "environment":
                environment.get_environment() is not None,

            "runtime_mode":
                DATA_MODE in ["paper", "live"],

            "broker_mode":
                BROKER_MODE in ["paper", "live"]

        }


        return {
            "status": "PASS" if all(checks.values()) else "FAIL",
            "checks": checks,
            "engine": "V3.34"
        }



v334_validator = V334Validator()
