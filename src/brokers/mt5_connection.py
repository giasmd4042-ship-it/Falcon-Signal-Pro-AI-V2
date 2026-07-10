from __future__ import annotations

import MetaTrader5 as mt5


class MT5Connection:
    def __init__(self):
        self._connected = False

    def connect(self) -> bool:
        self._connected = mt5.initialize()
        return self._connected

    def disconnect(self) -> None:
        if self._connected:
            mt5.shutdown()
            self._connected = False

    def is_connected(self) -> bool:
        return self._connected and mt5.terminal_info() is not None

    def account_info(self):
        if not self.is_connected():
            return None
        return mt5.account_info()

    def terminal_info(self):
        if not self.is_connected():
            return None
        return mt5.terminal_info()

    def last_error(self):
        return mt5.last_error()


mt5_connection = MT5Connection()
