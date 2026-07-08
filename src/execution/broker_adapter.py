from src.execution.exchange_connector import ExchangeConnector


class BrokerAdapter(ExchangeConnector):


    def __init__(self):

        self.connected = False


    def connect(self):

        self.connected = True

        return True


    def disconnect(self):

        self.connected = False

        return True


    def is_connected(self):

        return self.connected


    def get_account_info(self):

        return {
            "balance": 0,
            "currency": "USDT"
        }


    def place_order(self, order):

        if not self.connected:

            return None

        return order
