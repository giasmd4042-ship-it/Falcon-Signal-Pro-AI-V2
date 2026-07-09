class RealProviderInterface:


    def __init__(self):

        self.connected = False
        self.provider = "REAL_PROVIDER"
        self.error = None



    def connect(self):

        self.connected = False
        self.error = "PROVIDER_NOT_CONFIGURED"

        return False



    def disconnect(self):

        self.connected = False

        return True



    def get_price(self, symbol):

        if not self.connected:

            return None

        return None



    def submit_order(self, order):

        if not self.connected:

            return {

                "status": "BLOCKED",

                "reason": "PROVIDER_NOT_CONNECTED"

            }


        return {

            "status": "PENDING"

        }



    def get_status(self):

        return {

            "provider": self.provider,

            "connected": self.connected,

            "error": self.error,

            "engine": "V3.39"

        }



real_provider = RealProviderInterface()
