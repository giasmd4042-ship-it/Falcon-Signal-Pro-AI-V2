from src.security.live_permission_gate import live_permission_gate
from src.validation.v338_config_validator import production_config_validator
from src.validation.v337_runtime_validator import v337_runtime_validator


class V338DeploymentValidator:


    def validate(self):

        runtime = v337_runtime_validator.validate()

        config = production_config_validator.validate()

        live = live_permission_gate.validate()


        checks = {

            "runtime_layer":
                runtime["engine"] == "V3.37",


            "config_layer":
                config["engine"] == "V3.38",


            "permission_gate":
                live["status"] == "ALLOW" or live["status"] == "BLOCKED",


            "safety_active":
                live["checks"]["safety"]

        }


        return {


            "status":

                "READY"

                if all(checks.values())

                else "FAIL",



            "checks":

                checks,



            "live_permission":

                live["status"],



            "engine":

                "V3.38"

        }




v338_deployment_validator = V338DeploymentValidator()
