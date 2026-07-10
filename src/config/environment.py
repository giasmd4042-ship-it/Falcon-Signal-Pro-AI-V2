from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE if ENV_FILE.exists() else None)


@dataclass(frozen=True)
class EnvironmentConfig:
    app_env: str
    trading_mode: str
    log_level: str

    @property
    def is_development(self) -> bool:
        return self.app_env.lower() == "development"

    @property
    def is_paper(self) -> bool:
        return self.trading_mode.lower() == "paper"

    @property
    def is_live(self) -> bool:
        return self.trading_mode.lower() == "live"


def load_environment() -> EnvironmentConfig:
    return EnvironmentConfig(
        app_env=os.getenv("APP_ENV", "development"),
        trading_mode=os.getenv("TRADING_MODE", "paper"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )


environment = load_environment()
