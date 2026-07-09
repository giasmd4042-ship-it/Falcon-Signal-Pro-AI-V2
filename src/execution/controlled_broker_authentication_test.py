from src.security.real_credential_activation_manager import real_credential_activation_manager


class ControlledBrokerAuthenticationTest:


    def __init__(self):

        self.authenticated = False
        self.error = None



    def authenticate(self):


        credential = real_credential_activation_manager.activate()



        if not credential:

            self.authenticated = False
            self.error = "CREDENTIAL_ACTIVATION_FAILED"

            return False



        self.authenticated = True
        self.error = None

        return True



    def get_status(self):


        return {


            "authenticated":

                self.authenticated,



            "error":

                self.error,



            "engine":

                "V3.49"

        }




controlled_broker_authentication_test = ControlledBrokerAuthenticationTest()
