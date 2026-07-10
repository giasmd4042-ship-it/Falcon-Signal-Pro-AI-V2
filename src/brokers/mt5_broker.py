from __future__ import annotations

from typing import Any

import MetaTrader5 as mt5

from src.brokers.base_broker import BaseBroker
from src.brokers.mt5_connection import mt5_connection


class MT5Broker(BaseBroker):
    def connect(self) -> bool:
        return mt5_connection.connect()

    def disconnect(self) -> None:
        mt5_connection.disconnect()

    def is_connected(self) -> bool:
        return mt5_connection.is_connected()

    def place_order(self, order: dict[str, Any]) -> dict[str, Any]:
        symbol = order["symbol"]
        volume = float(order["volume"])

        if not mt5.symbol_select(symbol, True):
            return {"success": False, "error": "Cannot select symbol"}

        tick = mt5.symbol_info_tick(symbol)

        if tick is None:
            return {"success": False, "error": "No market tick"}

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

        check = mt5.order_check(request)

        if check is None or check.retcode != 0:
            return {
                "success": False,
                "stage": "order_check",
                "retcode": check.retcode if check else None,
                "comment": check.comment if check else str(mt5.last_error()),
            }

        result = mt5.order_send(request)

        if result is None:
            return {
                "success": False,
                "stage": "order_send",
                "error": str(mt5.last_error()),
            }

        return {
            "success": result.retcode == mt5.TRADE_RETCODE_DONE,
            "retcode": result.retcode,
            "order": result.order,
            "deal": result.deal,
            "volume": result.volume,
            "price": result.price,
            "comment": result.comment,
        }

    def cancel_order(self, order_id: str) -> bool:
        raise NotImplementedError("Pending order cancellation will be implemented later.")

    def get_positions(self) -> list[dict[str, Any]]:
        positions = mt5.positions_get()

        if positions is None:
            return []

        return [position._asdict() for position in positions]

    def get_account_summary(self) -> dict[str, Any]:
        info = mt5_connection.account_info()

        if info is None:
            return {}

        return {
            "login": info.login,
            "server": info.server,
            "company": info.company,
            "balance": info.balance,
            "equity": info.equity,
            "margin_free": info.margin_free,
            "currency": info.currency,
            "leverage": info.leverage,
            "trade_allowed": info.trade_allowed,
        }


mt5_broker = MT5Broker()
