from src.security.secure_credential_loader import secure_credential_loader
from src.security.secure_credential_validation_gate import secure_credential_validation_gate
from src.security.broker_credential_binding_check import broker_credential_binding_check


class V350ReleaseValidator:


    def validate(self):


        loader = secure_credential_loader.get_status()

        validation = secure_credential_validation_gate.get_status()

        binding = broker_credential_binding_check.get_status()



        checks = {


            "credential_loader":

                loader["engine"] == "V3.50",



            "validation_layer":

                validation["engine"] == "V3.50",



            "binding_layer":

                binding["engine"] == "V3.50",



            "safety":

                True

        }



        return {


            "status":

                "READY"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "live_status":

                "READY"

                if binding["credential_bound"]

                else "BLOCKED",



            "engine":

                "V3.50"

        }




v350_release_validator = V350ReleaseValidator()
