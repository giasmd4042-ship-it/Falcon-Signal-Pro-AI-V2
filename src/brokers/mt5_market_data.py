from __future__ import annotations

from typing import Any

import MetaTrader5 as mt5


class MT5MarketData:
    def symbol_select(self, symbol: str) -> bool:
        return mt5.symbol_select(symbol, True)

    def get_symbol_tick(self, symbol: str) -> dict[str, Any] | None:
        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            return None
        return tick._asdict()

    def get_symbol_info(self, symbol: str) -> dict[str, Any] | None:
        info = mt5.symbol_info(symbol)
        if info is None:
            return None
        return info._asdict()

    def get_rates(self, symbol: str, timeframe: int = mt5.TIMEFRAME_M1, count: int = 10) -> list:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)

        if rates is None:
            return []

        return rates.tolist()


mt5_market_data = MT5MarketData()
