from src.execution.broker_authentication_gateway import broker_authentication_gateway
from src.validation.connection_health_checker import connection_health_checker
from src.validation.live_data_handshake import live_data_handshake
from src.security.safety_guard import safety_guard


class ControlledActivationValidator:


    def validate(self):


        auth = broker_authentication_gateway.get_status()

        health = connection_health_checker.check()

        data = live_data_handshake.check()

        safety = safety_guard.allow_trade()



        checks = {


            "authentication":

                auth["authenticated"],



            "health":

                health["status"] == "HEALTHY",



            "data":

                data["status"] == "DATA_READY",



            "safety":

                safety

        }



        return {


            "status":

                "ACTIVATION_ALLOWED"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "engine":

                "V3.40"

        }




controlled_activation_validator = ControlledActivationValidator()
