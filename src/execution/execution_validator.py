from src.execution.order import OrderStatus


class ExecutionValidator:

    def validate(self, order):

        if not order.symbol:
            return False

        if order.quantity <= 0:
            return False

        if order.side is None:
            return False

        if order.status != OrderStatus.CREATED:
            return False

        return True
