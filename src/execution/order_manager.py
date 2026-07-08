from src.execution.order import OrderStatus


class OrderManager:

    def __init__(self):
        self.orders = {}


    def add_order(self, order):

        self.orders[order.order_id] = order
        return order


    def update_status(self, order_id, status):

        if order_id in self.orders:
            self.orders[order_id].status = status
            return self.orders[order_id]

        return None


    def get_order(self, order_id):

        return self.orders.get(order_id)


    def get_all_orders(self):

        return list(self.orders.values())


    def cancel_order(self, order_id):

        order = self.orders.get(order_id)

        if order:
            order.status = OrderStatus.CANCELLED
            return True

        return False
