from src.execution.live_broker_authentication_verifier import live_broker_authentication_verifier
from src.validation.live_account_permission_verifier import live_account_permission_verifier


class LiveSessionValidator:


    def __init__(self):

        self.connected = False
        self.error = None



    def validate(self):


        authentication = live_broker_authentication_verifier.verify()

        permission = live_account_permission_verifier.verify()



        if not authentication:

            self.connected = False
            self.error = "AUTHENTICATION_FAILED"

            return False



        if not permission:

            self.connected = False
            self.error = "ACCOUNT_PERMISSION_FAILED"

            return False



        self.connected = True
        self.error = None

        return True



    def get_status(self):


        return {


            "session_connected":

                self.connected,



            "error":

                self.error,



            "engine":

                "V3.47"

        }




live_session_validator = LiveSessionValidator()
