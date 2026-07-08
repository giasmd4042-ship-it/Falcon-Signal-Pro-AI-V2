from src.execution.base_broker import BaseBroker
from src.execution.order import OrderStatus


class PaperBroker(BaseBroker):

    def __init__(self, balance=10000):
        self.balance = balance
        self.orders = {}
        self.positions = {}

    def place_order(self, order):

        order.order_id = str(len(self.orders) + 1)
        order.status = OrderStatus.SUBMITTED

        order.fill(order.quantity)

        self.orders[order.order_id] = order

        self.positions[order.symbol] = {
            "quantity": order.filled_quantity,
            "side": order.side.value
        }

        return order


    def cancel_order(self, order_id):

        if order_id in self.orders:
            self.orders[order_id].cancel()
            return True

        return False


    def get_positions(self):
        return self.positions


    def get_balance(self):
        return self.balance
