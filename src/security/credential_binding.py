from src.security.api_key_manager import api_key_manager


class CredentialBinding:


    def validate(self):


        result = api_key_manager.validate_keys()


        return {


            "status":

                "READY"

                if result["valid"]

                else "BLOCKED",



            "keys":

                result["keys"],



            "engine":

                "V3.39"

        }




credential_binding = CredentialBinding()
