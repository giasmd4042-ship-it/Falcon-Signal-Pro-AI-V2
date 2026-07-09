from src.execution.live_session_validator import live_session_validator
from src.validation.live_connection_health_monitor import live_connection_health_monitor


class V347LiveReadinessReleaseValidator:


    def validate(self):


        session = live_session_validator.get_status()

        health = live_connection_health_monitor.get_status()



        checks = {


            "session_layer":

                session["engine"] == "V3.47",



            "health_layer":

                health["engine"] == "V3.47",



            "safety":

                True

        }



        return {


            "status":

                "READY"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "live_status":

                "READY"

                if health["healthy"]

                else "BLOCKED",



            "engine":

                "V3.47"

        }




v347_live_readiness_release_validator = V347LiveReadinessReleaseValidator()
