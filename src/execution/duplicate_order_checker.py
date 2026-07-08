class DuplicateOrderChecker:

    def __init__(self):

        self.order_history = []


    def is_duplicate(self, order):

        for existing in self.order_history:

            if (
                existing.symbol == order.symbol
                and existing.side == order.side
                and existing.quantity == order.quantity
            ):
                return True

        return False


    def add_order(self, order):

        self.order_history.append(order)
