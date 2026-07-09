from src.execution.broker_authentication_handler import broker_authentication_handler
from src.execution.account_permission_checker import account_permission_checker


class SessionVerification:


    def __init__(self):

        self.ready = False
        self.error = None



    def verify(self):


        authenticated = broker_authentication_handler.authenticate()

        permission = account_permission_checker.check()



        if not authenticated:

            self.ready = False
            self.error = "AUTHENTICATION_FAILED"

            return False



        if not permission:

            self.ready = False
            self.error = "PERMISSION_DENIED"

            return False



        self.ready = True
        self.error = None

        return True



    def get_status(self):


        return {


            "session_ready":

                self.ready,



            "error":

                self.error,



            "engine":

                "V3.42"

        }




session_verification = SessionVerification()
