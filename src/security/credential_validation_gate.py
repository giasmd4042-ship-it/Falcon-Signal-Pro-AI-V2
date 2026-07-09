from src.security.secure_credential_loader import secure_credential_loader
from src.security.safety_guard import safety_guard


class CredentialValidationGate:


    def validate(self):


        credentials = secure_credential_loader.validate()

        safety = safety_guard.allow_trade()



        checks = {


            "api_key":

                credentials["BROKER_API_KEY"],



            "secret_key":

                credentials["BROKER_SECRET_KEY"],



            "safety":

                safety

        }



        return {


            "status":

                "CREDENTIAL_READY"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "engine":

                "V3.41"

        }




credential_validation_gate = CredentialValidationGate()
