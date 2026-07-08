from src.signals.signal_provider import SignalProvider


class TrendFollowingSignal(SignalProvider):


    def __init__(self):

        self.name = "Trend Following"


    def generate(self, market_data):

        price = market_data.get_price("AAPL")


        if price > 150:

            return {
                "symbol": "AAPL",
                "signal": "BUY",
                "strategy": self.name
            }


        if price < 100:

            return {
                "symbol": "AAPL",
                "signal": "SELL",
                "strategy": self.name
            }


        return {
            "symbol": "AAPL",
            "signal": "HOLD",
            "strategy": self.name
        }
