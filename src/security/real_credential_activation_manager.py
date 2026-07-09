from src.security.live_credential_status_checker import live_credential_status_checker


class RealCredentialActivationManager:


    def __init__(self):

        self.active = False
        self.error = None



    def activate(self):


        status = live_credential_status_checker.check()



        if not status:

            self.active = False
            self.error = "CREDENTIAL_STATUS_NOT_READY"

            return False



        self.active = True
        self.error = None

        return True



    def get_status(self):


        return {


            "credential_active":

                self.active,



            "error":

                self.error,



            "engine":

                "V3.49"

        }




real_credential_activation_manager = RealCredentialActivationManager()
