class LivePositionMonitor:

    def __init__(self, position_manager):

        self.position_manager = position_manager


    def get_positions_snapshot(self):

        snapshot = []

        for position in self.position_manager.get_all_positions():

            snapshot.append(
                {
                    "symbol": position.symbol,
                    "quantity": position.quantity,
                    "side": position.side,
                    "entry_price": position.entry_price
                }
            )

        return snapshot


    def get_position_count(self):

        return len(
            self.position_manager.get_all_positions()
        )
