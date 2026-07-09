import os


class APIKeyManager:


    def __init__(self):

        self.required_keys = [
            "BROKER_API_KEY",
            "BROKER_SECRET_KEY"
        ]



    def get_key(self, name):

        return os.getenv(name)



    def has_key(self, name):

        return bool(self.get_key(name))



    def validate_keys(self):

        result = {}

        for key in self.required_keys:

            result[key] = self.has_key(key)


        return {

            "valid": all(result.values()),

            "keys": result,

            "engine": "V3.36"

        }



api_key_manager = APIKeyManager()
