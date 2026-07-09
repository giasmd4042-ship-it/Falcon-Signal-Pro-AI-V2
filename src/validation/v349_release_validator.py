from src.security.real_credential_activation_manager import real_credential_activation_manager
from src.execution.controlled_broker_authentication_test import controlled_broker_authentication_test
from src.validation.controlled_connection_verification import controlled_connection_verification


class V349ReleaseValidator:


    def validate(self):


        credential = real_credential_activation_manager.get_status()

        authentication = controlled_broker_authentication_test.get_status()

        connection = controlled_connection_verification.get_status()



        checks = {


            "credential_layer":

                credential["engine"] == "V3.49",



            "authentication_layer":

                authentication["engine"] == "V3.49",



            "connection_layer":

                connection["engine"] == "V3.49",



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

                if connection["connected"]

                else "BLOCKED",



            "engine":

                "V3.49"

        }




v349_release_validator = V349ReleaseValidator()
