from src.execution.real_broker_authentication_bridge import real_broker_authentication_bridge
from src.validation.live_account_verifier import live_account_verifier


class LiveConnectionHealthMonitor:


    def __init__(self):

        self.healthy = False
        self.error = None



    def check(self):


        authentication = real_broker_authentication_bridge.authenticate()

        account = live_account_verifier.verify()



        checks = {


            "authentication":

                authentication,



            "account":

                account

        }



        if not all(checks.values()):

            self.healthy = False
            self.error = "LIVE_CONNECTION_NOT_READY"

            return False



        self.healthy = True
        self.error = None

        return True



    def get_status(self):


        return {


            "healthy":

                self.healthy,



            "error":

                self.error,



            "engine":

                "V3.43"

        }




live_connection_health_monitor = LiveConnectionHealthMonitor()
