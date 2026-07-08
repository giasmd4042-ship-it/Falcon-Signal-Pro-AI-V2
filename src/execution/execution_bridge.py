from src.execution.order_execution_engine import OrderExecutionEngine


class ExecutionBridge:

    def __init__(self, execution_engine):

        self.execution_engine = execution_engine


    def submit_signal(self, signal):

        order = signal.to_order()

        return self.execution_engine.execute(order)


    def cancel_trade(self, order_id):

        return self.execution_engine.cancel(order_id)


    def get_execution_history(self):

        return self.execution_engine.get_orders()
