from src.data.live_market_data_adapter import live_market_data_adapter
from src.validation.connection_health_checker import connection_health_checker
from src.security.safety_guard import safety_guard


class LiveDataHandshake:


    def check(self):


        health = connection_health_checker.check()


        safety = safety_guard.allow_trade()


        data_status = live_market_data_adapter.get_status()



        checks = {


            "health":

                health["status"] == "HEALTHY",



            "data_adapter":

                data_status["connected"],



            "safety":

                safety

        }



        return {


            "status":

                "DATA_READY"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "data":

                data_status,



            "engine":

                "V3.40"

        }




live_data_handshake = LiveDataHandshake()
