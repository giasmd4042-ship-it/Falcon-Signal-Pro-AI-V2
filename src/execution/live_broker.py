class LiveBroker:


    def __init__(self):

        self.connected = False
        self.orders = {}
        self.positions = {}


    def connect(self):

        self.connected = True
        return True


    def place_order(self, order):

        if not self.connected:
            raise Exception("Broker not connected")

        order.status = order.status
        self.orders[order.order_id] = order

        return order


    def cancel_order(self, order_id):

        if order_id in self.orders:
            return True

        return False


    def get_positions(self):

        return self.positions



live_broker = LiveBroker()
