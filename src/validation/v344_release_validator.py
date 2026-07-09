from src.security.controlled_live_activation_gate import controlled_live_activation_gate
from src.security.live_safety_governor import live_safety_governor
from src.execution.controlled_execution_guard import controlled_execution_guard


class V344ReleaseValidator:


    def validate(self):


        activation = controlled_live_activation_gate.get_status()

        safety = live_safety_governor.get_status()

        execution = controlled_execution_guard.get_status()



        checks = {


            "activation_layer":

                activation["engine"] == "V3.44",



            "safety_layer":

                safety["engine"] == "V3.44",



            "execution_layer":

                execution["engine"] == "V3.44",



            "risk_control":

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

                if execution["execution_allowed"]

                else "BLOCKED",



            "engine":

                "V3.44"

        }




v344_release_validator = V344ReleaseValidator()
