from src.security.controlled_live_activation_gate import controlled_live_activation_gate


class LiveSafetyGovernor:


    def __init__(self):

        self.allowed = False
        self.reason = None



    def authorize(self):


        activation = controlled_live_activation_gate.validate()



        if not activation:

            self.allowed = False
            self.reason = "CONTROLLED_LIVE_BLOCKED"

            return False



        self.allowed = True
        self.reason = None

        return True



    def get_status(self):


        return {


            "safety_authorized":

                self.allowed,



            "reason":

                self.reason,



            "engine":

                "V3.44"

        }




live_safety_governor = LiveSafetyGovernor()
