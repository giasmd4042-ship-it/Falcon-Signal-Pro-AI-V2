import json
import os


class TradingConfig:

    def __init__(self, path="config/trading_config.json"):

        self.path = path
        self.data = self.load()


    def load(self):

        if not os.path.exists(self.path):
            return {}

        with open(self.path, "r") as file:
            return json.load(file)


    def get(self, key, default=None):

        return self.data.get(key, default)


config = TradingConfig()
