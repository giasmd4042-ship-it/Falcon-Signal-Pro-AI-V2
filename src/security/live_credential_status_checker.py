from src.security.secure_credential_loader import secure_credential_loader


class LiveCredentialStatusChecker:


    def __init__(self):

        self.ready = False
        self.error = None



    def check(self):


        credential = secure_credential_loader.validate()



        if not credential["valid"]:

            self.ready = False
            self.error = "CREDENTIALS_NOT_READY"

            return False



        self.ready = True
        self.error = None

        return True



    def get_status(self):


        return {


            "credential_ready":

                self.ready,



            "error":

                self.error,



            "engine":

                "V3.46"

        }




live_credential_status_checker = LiveCredentialStatusChecker()
