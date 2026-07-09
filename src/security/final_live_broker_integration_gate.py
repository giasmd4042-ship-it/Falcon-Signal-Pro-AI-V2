from src.validation.v347_live_readiness_release_validator import v347_live_readiness_release_validator


class FinalLiveBrokerIntegrationGate:


    def __init__(self):

        self.ready = False
        self.error = None



    def validate(self):


        readiness = v347_live_readiness_release_validator.validate()



        if readiness["live_status"] != "READY":

            self.ready = False
            self.error = "V347_LIVE_STATUS_BLOCKED"

            return False



        self.ready = True
        self.error = None

        return True



    def get_status(self):


        return {


            "final_live_ready":

                self.ready,



            "error":

                self.error,



            "engine":

                "V3.48"

        }




final_live_broker_integration_gate = FinalLiveBrokerIntegrationGate()
