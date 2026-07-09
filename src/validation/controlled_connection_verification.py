from src.execution.controlled_broker_authentication_test import controlled_broker_authentication_test


class ControlledConnectionVerification:


    def __init__(self):

        self.connected = False
        self.error = None



    def verify(self):


        authentication = controlled_broker_authentication_test.authenticate()



        if not authentication:

            self.connected = False
            self.error = "BROKER_AUTHENTICATION_FAILED"

            return False



        self.connected = True
        self.error = None

        return True



    def get_status(self):


        return {


            "connected":

                self.connected,



            "error":

                self.error,



            "engine":

                "V3.49"

        }




controlled_connection_verification = ControlledConnectionVerification()
