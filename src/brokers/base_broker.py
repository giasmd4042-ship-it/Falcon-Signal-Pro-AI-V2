from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseBroker(ABC):
    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def place_order(self, order: dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def cancel_order(self, order_id: str) -> bool:
        pass

    @abstractmethod
    def get_positions(self) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def get_account_summary(self) -> dict[str, Any]:
        pass
