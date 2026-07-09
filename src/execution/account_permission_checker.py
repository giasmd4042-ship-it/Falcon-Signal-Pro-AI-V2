from src.execution.broker_authentication_handler import broker_authentication_handler


class AccountPermissionChecker:


    def __init__(self):

        self.allowed = False
        self.error = None



    def check(self):


        authenticated = broker_authentication_handler.authenticate()



        if not authenticated:

            self.allowed = False
            self.error = "AUTHENTICATION_REQUIRED"

            return False



        self.allowed = True
        self.error = None

        return True



    def get_status(self):


        return {


            "trading_allowed":

                self.allowed,



            "error":

                self.error,



            "engine":

                "V3.42"

        }




account_permission_checker = AccountPermissionChecker()
