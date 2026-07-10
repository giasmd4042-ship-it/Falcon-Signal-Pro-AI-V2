from src.security.secure_credential_loader import secure_credential_loader


class SecureCredentialValidationGate:


    def __init__(self):

        self.valid = False
        self.error = None



    def validate(self):


        loaded = secure_credential_loader.load()



        if not loaded:

            self.valid = False

            self.error = "CREDENTIALS_NOT_AVAILABLE"

            return False



        self.valid = True

        self.error = None

        return True



    def get_status(self):


        return {


            "credential_valid":

                self.valid,



            "error":

                self.error,



            "engine":

                "V3.50"

        }




secure_credential_validation_gate = SecureCredentialValidationGate()
