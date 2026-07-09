from src.core.config import VERSION, DATA_MODE, BROKER_MODE
from src.data.data_factory import data_factory
from src.execution.broker_factory import broker_factory
from src.validation.live_safety_validator import live_safety_validator


class V336ReleaseValidator:


    def validate(self):

        data_provider = data_factory.create()
        broker_provider = broker_factory.create()

        safety = live_safety_validator.validate()


        checks = {

            "version":
                VERSION == "3.36.0",

            "data_factory":
                data_provider is not None,

            "broker_factory":
                broker_provider is not None,

            "data_mode":
                DATA_MODE in ["paper", "live"],

            "broker_mode":
                BROKER_MODE in ["paper", "live"],

            "safety_layer":
                safety["status"] in ["READY", "BLOCKED"]

        }


        return {

            "status":
                "READY" if all(checks.values()) else "FAIL",

            "checks":
                checks,

            "data_provider":
                type(data_provider).__name__,

            "broker_provider":
                type(broker_provider).__name__,

            "live_status":
                safety["status"],

            "engine":
                "V3.36"

        }



v336_release_validator = V336ReleaseValidator()
