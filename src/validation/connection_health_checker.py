from src.execution.live_connection_manager import live_connection_manager
from src.security.safety_guard import safety_guard


class ConnectionHealthChecker:


    def check(self):


        connection = live_connection_manager.get_status()


        safety = safety_guard.allow_trade()



        checks = {


            "connection":

                connection["connected"],



            "authentication":

                connection["error"] != "AUTHENTICATION_FAILED",



            "safety":

                safety

        }



        return {


            "status":

                "HEALTHY"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "connection":

                connection,



            "engine":

                "V3.40"

        }




connection_health_checker = ConnectionHealthChecker()
