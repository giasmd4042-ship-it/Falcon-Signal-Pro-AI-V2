from src.security.safety_guard import safety_guard


class BrokerOrderGateway:


    def __init__(self, client):

        self.client = client
        self.orders = {}



    def submit_order(self, order):

        if not safety_guard.allow_trade():

            return {

                "status": "BLOCKED",

                "reason": "SAFETY_STOP"

            }



        if not self.client.connected:

            return {

                "status": "BLOCKED",

                "reason": "BROKER_NOT_CONNECTED"

            }



        order_id = str(len(self.orders) + 1)


        self.orders[order_id] = order


        return {

            "status": "SUBMITTED",

            "order_id": order_id,

            "order": order

        }



    def cancel_order(self, order_id):

        if order_id in self.orders:

            del self.orders[order_id]

            return True


        return False



    def get_orders(self):

        return self.orders



