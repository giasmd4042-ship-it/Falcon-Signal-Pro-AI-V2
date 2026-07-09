from src.security.live_credential_status_checker import live_credential_status_checker


class LiveBrokerAuthenticationVerifier:


    def __init__(self):

        self.authenticated = False
        self.error = None



    def verify(self):


        credential = live_credential_status_checker.check()



        if not credential:

            self.authenticated = False
            self.error = "CREDENTIALS_NOT_READY"

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

                "V3.46"

        }




live_broker_authentication_verifier = LiveBrokerAuthenticationVerifier()
