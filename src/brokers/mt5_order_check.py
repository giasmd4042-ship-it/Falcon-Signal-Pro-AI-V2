from __future__ import annotations

import MetaTrader5 as mt5


def check_market_buy(symbol: str = "EURUSDm", volume: float = 0.01):
    tick = mt5.symbol_info_tick(symbol)

    if tick is None:
        return None

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY,
        "price": tick.ask,
        "deviation": 20,
        "type_filling": mt5.ORDER_FILLING_FOK,
        "type_time": mt5.ORDER_TIME_GTC,
    }

    return mt5.order_check(request)
