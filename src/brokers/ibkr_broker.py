from __future__ import annotations

from ib_insync import IB

from src.brokers.base_broker import BaseBroker
from src.config.broker_config import broker_config


class IBKRBroker(BaseBroker):
    def __init__(self) -> None:
        self._ib = IB()

    def connect(self) -> bool:
        if self._ib.isConnected():
            return True

        try:
            self._ib.connect(
                host=broker_config.host,
                port=broker_config.port,
                clientId=broker_config.client_id,
                timeout=10,
            )
            return self._ib.isConnected()
        except Exception:
            return False

    def disconnect(self) -> None:
        if self._ib.isConnected():
            self._ib.disconnect()

    def is_connected(self) -> bool:
        return self._ib.isConnected()

    def place_order(self, order: dict):
        raise NotImplementedError("Order placement will be implemented in V3.52")

    def cancel_order(self, order_id: str) -> bool:
        raise NotImplementedError("Order cancellation will be implemented in V3.52")

    def get_positions(self) -> list:
        raise NotImplementedError("Position retrieval will be implemented in V3.52")

    def get_account_summary(self) -> dict:
        raise NotImplementedError("Account summary will be implemented in V3.52")
