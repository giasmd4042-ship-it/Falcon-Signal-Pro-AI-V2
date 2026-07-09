from src.validation.v337_runtime_validator import v337_runtime_validator
from src.data.live_market_data_adapter import live_market_data_adapter


class V337ReleaseValidator:


    def validate(self):

        runtime = v337_runtime_validator.validate()

        checks = {

            "runtime_validator":
                runtime["engine"] == "V3.37",

            "market_adapter":
                live_market_data_adapter.get_status()["provider"]
                == "LIVE_DATA_ADAPTER",

            "safety_response":
                runtime["order_test"]["status"]
                == "BLOCKED"

        }


        return {

            "status":
                "READY" if all(checks.values()) else "FAIL",

            "checks":
                checks,

            "runtime":
                runtime,

            "engine":
                "V3.37"

        }



v337_release_validator = V337ReleaseValidator()
