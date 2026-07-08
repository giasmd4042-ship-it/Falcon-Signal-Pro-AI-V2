"""
Falcon Signal Pro AI V2.0
Configuration Module
"""

APP_NAME = "Falcon Signal Pro AI V2.0"
VERSION = "3.34.0"


ASSETS = [
    "BTCUSDT",
    "XAUUSD"
]


TIMEFRAMES = [
    "1H",
    "30M",
    "5M"
]


MAX_ACTIVE_SIGNAL = 1


ENABLE_TELEGRAM = False
ENABLE_DASHBOARD = False


# V3.34 Runtime Modes

DATA_MODE = "paper"

BROKER_MODE = "paper"


ENABLE_LIVE_TRADING = False
ENABLE_PAPER_TRADING = True
