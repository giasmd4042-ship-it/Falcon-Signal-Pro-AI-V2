import os


class SecureCredentialLoader:


    def get_broker_key(self):

        return os.getenv("BROKER_API_KEY")



    def get_broker_secret(self):

        return os.getenv("BROKER_SECRET_KEY")



    def validate(self):


        key = self.get_broker_key()

        secret = self.get_broker_secret()



        return {


            "valid":

                bool(key and secret),



            "BROKER_API_KEY":

                bool(key),



            "BROKER_SECRET_KEY":

                bool(secret),



            "engine":

                "V3.41"

        }




secure_credential_loader = SecureCredentialLoader()
