from src.execution.order_manager import OrderManager


class OrderExecutionEngine:

    def __init__(self, broker):

        self.broker = broker
        self.order_manager = OrderManager()


    def execute(self, order):

        result = self.broker.place_order(order)

        self.order_manager.add_order(result)

        return result


    def cancel(self, order_id):

        broker_result = self.broker.cancel_order(order_id)

        manager_result = self.order_manager.cancel_order(order_id)

        return broker_result and manager_result


    def get_orders(self):

        return self.order_manager.get_all_orders()
