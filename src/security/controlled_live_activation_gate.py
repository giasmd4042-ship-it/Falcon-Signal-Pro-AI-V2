from src.validation.v343_release_validator import v343_release_validator


class ControlledLiveActivationGate:


    def __init__(self):

        self.ready = False
        self.error = None



    def validate(self):


        release = v343_release_validator.validate()



        if release["live_status"] != "READY":

            self.ready = False
            self.error = "V343_LIVE_STATUS_BLOCKED"

            return False



        self.ready = True
        self.error = None

        return True



    def get_status(self):


        return {


            "controlled_live_ready":

                self.ready,



            "error":

                self.error,



            "engine":

                "V3.44"

        }




controlled_live_activation_gate = ControlledLiveActivationGate()
