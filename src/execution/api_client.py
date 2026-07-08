class APIClient:


    def __init__(self, api_key=None, api_secret=None):

        self.api_key = api_key
        self.api_secret = api_secret


    def authenticate(self):

        return (
            self.api_key is not None
            and self.api_secret is not None
        )


    def request(self, endpoint, payload=None):

        return {
            "endpoint": endpoint,
            "payload": payload,
            "status": "success"
        }
