class TradeSynchronizer:

    def __init__(self, broker, position_manager):

        self.broker = broker
        self.position_manager = position_manager


    def synchronize(self):

        broker_positions = self.broker.get_positions()

        for symbol, data in broker_positions.items():

            position = self.position_manager.get_position(symbol)

            if position:

                position.update_quantity(
                    data["quantity"]
                )

            else:

                from src.execution.position_manager import Position

                new_position = Position(
                    symbol=symbol,
                    quantity=data["quantity"],
                    entry_price=0,
                    side=data["side"]
                )

                self.position_manager.add_position(
                    new_position
                )

        return self.position_manager.get_all_positions()
