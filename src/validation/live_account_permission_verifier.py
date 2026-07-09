from src.execution.live_broker_authentication_verifier import live_broker_authentication_verifier


class LiveAccountPermissionVerifier:


    def __init__(self):

        self.permission = False
        self.error = None



    def verify(self):


        authenticated = live_broker_authentication_verifier.verify()



        if not authenticated:

            self.permission = False
            self.error = "BROKER_AUTHENTICATION_REQUIRED"

            return False



        self.permission = True
        self.error = None

        return True



    def get_status(self):


        return {


            "trading_permission":

                self.permission,



            "error":

                self.error,



            "engine":

                "V3.46"

        }




live_account_permission_verifier = LiveAccountPermissionVerifier()
