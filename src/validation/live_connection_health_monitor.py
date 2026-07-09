from src.execution.live_session_validator import live_session_validator


class LiveConnectionHealthMonitor:


    def __init__(self):

        self.healthy = False
        self.error = None



    def check(self):


        session = live_session_validator.validate()



        if not session:

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

                "V3.47"

        }




live_connection_health_monitor = LiveConnectionHealthMonitor()
