from src.security.secure_credential_validation_gate import secure_credential_validation_gate


class BrokerCredentialBindingCheck:


    def __init__(self):

        self.bound = False
        self.error = None



    def bind(self):


        valid = secure_credential_validation_gate.validate()



        if not valid:

            self.bound = False

            self.error = "CREDENTIAL_VALIDATION_FAILED"

            return False



        self.bound = True

        self.error = None

        return True



    def get_status(self):


        return {


            "credential_bound":

                self.bound,



            "error":

                self.error,



            "engine":

                "V3.50"

        }




broker_credential_binding_check = BrokerCredentialBindingCheck()
