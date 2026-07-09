from src.security.secure_credential_loader import secure_credential_loader


class CredentialActivationManager:


    def __init__(self):

        self.active = False
        self.error = None



    def activate(self):


        result = secure_credential_loader.validate()



        if not result["valid"]:

            self.active = False
            self.error = "CREDENTIALS_NOT_AVAILABLE"

            return False



        self.active = True
        self.error = None

        return True



    def get_status(self):


        return {


            "credential_active":

                self.active,



            "error":

                self.error,



            "engine":

                "V3.43"

        }




credential_activation_manager = CredentialActivationManager()
