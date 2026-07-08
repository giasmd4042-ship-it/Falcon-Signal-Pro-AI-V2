from abc import ABC, abstractmethod


class ExchangeConnector(ABC):


    @abstractmethod
    def connect(self):

        pass


    @abstractmethod
    def disconnect(self):

        pass


    @abstractmethod
    def is_connected(self):

        pass


    @abstractmethod
    def get_account_info(self):

        pass


    @abstractmethod
    def place_order(self, order):

        pass
