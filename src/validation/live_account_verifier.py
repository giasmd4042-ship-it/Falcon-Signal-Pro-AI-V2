from src.execution.real_broker_authentication_bridge import real_broker_authentication_bridge


class LiveAccountVerifier:


    def __init__(self):

        self.ready = False
        self.error = None



    def verify(self):


        authenticated = real_broker_authentication_bridge.authenticate()



        if not authenticated:

            self.ready = False
            self.error = "BROKER_AUTHENTICATION_FAILED"

            return False



        self.ready = True
        self.error = None

        return True



    def get_status(self):


        return {


            "account_ready":

                self.ready,



            "error":

                self.error,



            "engine":

                "V3.43"

        }




live_account_verifier = LiveAccountVerifier()
