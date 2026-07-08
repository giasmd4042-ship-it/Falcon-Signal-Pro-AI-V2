from dataclasses import dataclass


@dataclass
class Position:

    symbol: str
    quantity: float
    entry_price: float
    side: str

    def update_quantity(self, quantity):

        self.quantity = quantity


    def calculate_pnl(self, current_price):

        if self.side == "LONG":
            return (current_price - self.entry_price) * self.quantity

        if self.side == "SHORT":
            return (self.entry_price - current_price) * self.quantity

        return 0


class PositionManager:

    def __init__(self):

        self.positions = {}


    def add_position(self, position):

        self.positions[position.symbol] = position

        return position


    def get_position(self, symbol):

        return self.positions.get(symbol)


    def remove_position(self, symbol):

        if symbol in self.positions:

            del self.positions[symbol]

            return True

        return False


    def get_all_positions(self):

        return list(self.positions.values())
