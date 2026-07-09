from src.security.final_live_broker_integration_gate import final_live_broker_integration_gate
from src.validation.live_connection_health_monitor import live_connection_health_monitor


class FinalBrokerConnectionHealthConfirmation:


    def __init__(self):

        self.connected = False
        self.error = None



    def confirm(self):


        activation = final_live_broker_integration_gate.validate()

        health = live_connection_health_monitor.check()



        checks = {


            "activation_gate":

                activation,



            "connection_health":

                health

        }



        if not all(checks.values()):

            self.connected = False
            self.error = "FINAL_CONNECTION_BLOCKED"

            return False



        self.connected = True
        self.error = None

        return True



    def get_status(self):


        return {


            "connection_ready":

                self.connected,



            "error":

                self.error,



            "engine":

                "V3.48"

        }




final_broker_connection_health_confirmation = FinalBrokerConnectionHealthConfirmation()
