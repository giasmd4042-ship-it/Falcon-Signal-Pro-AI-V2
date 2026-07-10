from __future__ import annotations

from typing import Any

import MetaTrader5 as mt5


class MT5ExecutionValidator:
    def validate(self, symbol: str, volume: float) -> tuple[bool, str]:
        info = mt5.symbol_info(symbol)

        if info is None:
            return False, "Symbol not found"

        if not info.visible:
            if not mt5.symbol_select(symbol, True):
                return False, "Cannot enable symbol"

        terminal = mt5.terminal_info()

        if terminal is None or not terminal.trade_allowed:
            return False, "Terminal trading disabled"

        account = mt5.account_info()

        if account is None or not account.trade_allowed:
            return False, "Account trading disabled"

        if volume < info.volume_min:
            return False, f"Minimum volume is {info.volume_min}"

        if volume > info.volume_max:
            return False, f"Maximum volume is {info.volume_max}"

        step = info.volume_step

        if round(volume / step) * step != volume:
            return False, f"Volume must be a multiple of {step}"

        return True, "OK"


mt5_execution_validator = MT5ExecutionValidator()
