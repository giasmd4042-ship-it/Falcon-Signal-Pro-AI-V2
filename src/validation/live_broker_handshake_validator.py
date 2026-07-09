from src.execution.broker_session_manager import broker_session_manager
from src.execution.live_connection_manager import live_connection_manager
from src.security.safety_guard import safety_guard


class LiveBrokerHandshakeValidator:


    def validate(self):


        session = broker_session_manager.authenticate()

        connection = live_connection_manager.connect()

        safety = safety_guard.allow_trade()



        checks = {


            "session":

                session,



            "connection":

                connection,



            "safety":

                safety

        }



        return {


            "status":

                "BROKER_READY"

                if all(checks.values())

                else "BLOCKED",



            "checks":

                checks,



            "engine":

                "V3.41"

        }




live_broker_handshake_validator = LiveBrokerHandshakeValidator()
