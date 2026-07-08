from abc import ABC, abstractmethod


class BaseBroker(ABC):

    @abstractmethod
    def place_order(self, order):
        pass

    @abstractmethod
    def cancel_order(self, order_id):
        pass

    @abstractmethod
    def get_positions(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass
