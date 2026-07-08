from src.core.config import BROKER_MODE

from src.execution.paper_broker import PaperBroker
from src.execution.live_broker import LiveBroker


class BrokerAdapter:

    def __init__(self, mode=BROKER_MODE):

        self.mode = mode

        if mode == "live":
            self.broker = LiveBroker()

        else:
            self.broker = PaperBroker()


    def connect(self):

        if hasattr(self.broker, "connect"):
            return self.broker.connect()

        return True


    def place_order(self, order):

        return self.broker.place_order(order)


    def submit_order(self, order):

        return self.place_order(order)


    def cancel_order(self, order_id):

        return self.broker.cancel_order(order_id)


    def positions(self):

        return self.broker.get_positions()


    def balance(self):

        if hasattr(self.broker, "get_balance"):
            return self.broker.get_balance()

        return 0



broker_adapter = BrokerAdapter()
