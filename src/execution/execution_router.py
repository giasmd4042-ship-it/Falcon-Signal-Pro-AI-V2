from __future__ import annotations

from typing import Any


class ExecutionRouter:
    def __init__(self) -> None:
        self._brokers: dict[str, Any] = {}

    def register_broker(self, name: str, broker: Any) -> None:
        self._brokers[name.lower()] = broker

    def get_broker(self, name: str) -> Any:
        broker = self._brokers.get(name.lower())

        if broker is None:
            raise ValueError(f"Broker '{name}' is not registered.")

        return broker

    def place_order(self, broker_name: str, order: dict[str, Any]) -> Any:
        broker = self.get_broker(broker_name)
        return broker.place_order(order)


execution_router = ExecutionRouter()
