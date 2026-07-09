from src.execution.broker_authentication_gateway import broker_authentication_gateway


class LiveConnectionManager:


    def __init__(self):

        self.connected = False
        self.error = None



    def connect(self):


        authenticated = broker_authentication_gateway.authenticate()


        if not authenticated:

            self.connected = False
            self.error = "AUTHENTICATION_FAILED"

            return False



        self.connected = True
        self.error = None

        return True



    def disconnect(self):

        self.connected = False

        return True



    def get_status(self):

        return {

            "connected": self.connected,

            "error": self.error,

            "engine": "V3.40"

        }




live_connection_manager = LiveConnectionManager()
