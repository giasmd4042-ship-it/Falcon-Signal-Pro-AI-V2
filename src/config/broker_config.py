from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class BrokerConfig:
    host: str
    port: int
    client_id: int
    account: str | None

    @property
    def is_paper(self) -> bool:
        return self.port == 7497

    @property
    def is_live(self) -> bool:
        return self.port == 7496


def load_broker_config() -> BrokerConfig:
    return BrokerConfig(
        host=os.getenv("IBKR_HOST", "127.0.0.1"),
        port=int(os.getenv("IBKR_PORT", "7497")),
        client_id=int(os.getenv("IBKR_CLIENT_ID", "1")),
        account=os.getenv("IBKR_ACCOUNT") or None,
    )


broker_config = load_broker_config()
