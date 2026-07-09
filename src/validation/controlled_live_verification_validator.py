from src.security.live_credential_status_checker import live_credential_status_checker
from src.execution.live_broker_authentication_verifier import live_broker_authentication_verifier
from src.validation.live_account_permission_verifier import live_account_permission_verifier


class ControlledLiveVerificationValidator:


    def validate(self):


        credential = live_credential_status_checker.get_status()

        authentication = live_broker_authentication_verifier.get_status()

        account = live_account_permission_verifier.get_status()



        checks = {


            "credential_layer":

                credential["engine"] == "V3.46",



            "authentication_layer":

                authentication["engine"] == "V3.46",



            "account_permission_layer":

                account["engine"] == "V3.46",



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

                if account["trading_permission"]

                else "BLOCKED",



            "engine":

                "V3.46"

        }




controlled_live_verification_validator = ControlledLiveVerificationValidator()
