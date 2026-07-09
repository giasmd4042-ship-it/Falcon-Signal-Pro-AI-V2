from src.validation.v339_runtime_provider_validator import v339_runtime_provider_validator
from src.security.credential_binding import credential_binding
from src.security.safety_guard import safety_guard


class V339ReleaseValidator:


    def validate(self):


        runtime = v339_runtime_provider_validator.validate()

        credentials = credential_binding.validate()


        checks = {


            "runtime":

                runtime["status"] == "PASS",



            "data_provider":

                runtime["data_provider"] is not None,



            "broker_provider":

                runtime["broker_provider"] is not None,



            "credential_layer":

                credentials["engine"] == "V3.39",



            "safety":

                safety_guard.allow_trade()

        }



        return {


            "status":

                "READY"

                if all(checks.values())

                else "FAIL",



            "checks":

                checks,



            "credential_status":

                credentials["status"],



            "runtime":

                runtime,



            "engine":

                "V3.39"

        }




v339_release_validator = V339ReleaseValidator()
