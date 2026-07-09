from src.security.live_safety_governor import live_safety_governor


class ControlledExecutionGuard:


    def __init__(self):

        self.allowed = False
        self.error = None



    def check(self):


        safety = live_safety_governor.authorize()



        if not safety:

            self.allowed = False
            self.error = "SAFETY_PERMISSION_BLOCKED"

            return False



        self.allowed = True
        self.error = None

        return True



    def get_status(self):


        return {


            "execution_allowed":

                self.allowed,



            "error":

                self.error,



            "engine":

                "V3.44"

        }




controlled_execution_guard = ControlledExecutionGuard()
