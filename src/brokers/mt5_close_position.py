from __future__ import annotations

import MetaTrader5 as mt5


def close_position(ticket: int) -> dict:
    positions = mt5.positions_get(ticket=ticket)

    if not positions:
        return {"success": False, "error": "Position not found"}

    position = positions[0]
    tick = mt5.symbol_info_tick(position.symbol)

    if tick is None:
        return {"success": False, "error": "No market tick"}

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "position": position.ticket,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt5.ORDER_TYPE_SELL if position.type == mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY,
        "price": tick.bid if position.type == mt5.POSITION_TYPE_BUY else tick.ask,
        "deviation": 20,
        "type_filling": mt5.ORDER_FILLING_FOK,
        "type_time": mt5.ORDER_TIME_GTC,
    }

    result = mt5.order_send(request)

    if result is None:
        return {"success": False, "error": str(mt5.last_error())}

    return {
        "success": result.retcode == mt5.TRADE_RETCODE_DONE,
        "retcode": result.retcode,
        "deal": result.deal,
        "order": result.order,
        "comment": result.comment,
    }
