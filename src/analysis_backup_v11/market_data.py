"""
Falcon Signal Pro AI V2.0
Market Data Module
"""

import yfinance as yf


class MarketData:

    def get_data(self, symbol: str, interval: str = "1h", period: str = "7d"):

        data = yf.download(
            tickers=symbol,
            interval=interval,
            period=period,
            progress=False,
            auto_adjust=True,
        )

        return data
