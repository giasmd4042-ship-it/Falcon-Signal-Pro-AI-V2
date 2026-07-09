from src.validation.connection_health_checker import connection_health_checker
from src.validation.live_data_handshake import live_data_handshake
from src.validation.controlled_activation_validator import controlled_activation_validator
from src.execution.broker_authentication_gateway import broker_authentication_gateway


class V340ReleaseValidator:


    def validate(self):


        auth = broker_authentication_gateway.get_status()

        health = connection_health_checker.check()

        data = live_data_handshake.check()

        activation = controlled_activation_validator.validate()



        checks = {


            "authentication_layer":

                auth is not None,



            "health_layer":

                health["engine"] == "V3.40",



            "data_handshake":

                data["engine"] == "V3.40",



            "activation_gate":

                activation["engine"] == "V3.40",



            "safety":

                activation["checks"]["safety"]

        }



        return {


            "status":

                "READY"

                if all(checks.values())

                else "FAIL",



            "checks":

                checks,



            "live_status":

                activation["status"],



            "engine":

                "V3.40"

        }




v340_release_validator = V340ReleaseValidator()
