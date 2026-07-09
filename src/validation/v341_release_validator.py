from src.security.secure_credential_loader import secure_credential_loader
from src.security.credential_validation_gate import credential_validation_gate
from src.security.broker_credential_binding import broker_credential_binding
from src.execution.broker_session_manager import broker_session_manager
from src.validation.live_broker_handshake_validator import live_broker_handshake_validator


class V341ReleaseValidator:


    def validate(self):


        credentials = secure_credential_loader.validate()

        gate = credential_validation_gate.validate()

        binding = broker_credential_binding.get_status()

        session = broker_session_manager.get_status()

        handshake = live_broker_handshake_validator.validate()



        checks = {


            "credential_layer":

                credentials is not None,



            "validation_gate":

                gate["engine"] == "V3.41",



            "binding_layer":

                binding["engine"] == "V3.41",



            "session_layer":

                session["engine"] == "V3.41",



            "handshake_layer":

                handshake["engine"] == "V3.41",



            "safety":

                gate["checks"]["safety"]

        }



        return {


            "status":

                "READY"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "broker_status":

                handshake["status"],



            "engine":

                "V3.41"

        }




v341_release_validator = V341ReleaseValidator()
