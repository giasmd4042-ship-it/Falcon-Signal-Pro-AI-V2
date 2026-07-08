import os


class APIKeyManager:


    def get_key(self, name):

        return os.getenv(name)


    def has_key(self, name):

        return bool(self.get_key(name))



api_key_manager = APIKeyManager()
