import os


class SecureCredentialLoader:


    def __init__(self):

        self.loaded = False
        self.error = None



    def load(self):


        required = [

            "BROKER_API_KEY",

            "BROKER_API_SECRET"

        ]



        missing = [

            item

            for item in required

            if not os.getenv(item)

        ]



        if missing:

            self.loaded = False

            self.error = "MISSING_SECURE_CREDENTIALS"

            return False



        self.loaded = True

        self.error = None

        return True



    def validate(self):


        result = self.load()


        return {


            "valid":

                result,



            "error":

                self.error,



            "engine":

                "V3.50"

        }



    def get_status(self):


        return {


            "credentials_loaded":

                self.loaded,



            "error":

                self.error,



            "engine":

                "V3.50"

        }




secure_credential_loader = SecureCredentialLoader()
