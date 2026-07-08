from abc import ABC, abstractmethod


class SignalProvider(ABC):


    @abstractmethod
    def generate(self, market_data):

        pass
