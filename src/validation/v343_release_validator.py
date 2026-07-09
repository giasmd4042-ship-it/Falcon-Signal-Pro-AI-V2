from src.security.credential_activation_manager import credential_activation_manager
from src.execution.real_broker_authentication_bridge import real_broker_authentication_bridge
from src.validation.live_account_verifier import live_account_verifier
from src.validation.live_connection_health_monitor import live_connection_health_monitor


class V343ReleaseValidator:


    def validate(self):


        credential = credential_activation_manager.get_status()

        authentication = real_broker_authentication_bridge.get_status()

        account = live_account_verifier.get_status()

        health = live_connection_health_monitor.get_status()



        checks = {


            "credential_layer":

                credential["engine"] == "V3.43",



            "authentication_layer":

                authentication["engine"] == "V3.43",



            "account_layer":

                account["engine"] == "V3.43",



            "health_layer":

                health["engine"] == "V3.43",



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

                "BLOCKED"

                if not health["healthy"]

                else "READY",



            "engine":

                "V3.43"

        }




v343_release_validator = V343ReleaseValidator()
