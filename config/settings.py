import os


APP_NAME = "Falcon-Signal-Pro-AI-V2"

VERSION = "V3.33.x"

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)


MODE = os.getenv(
    "MODE",
    "paper"
)


API_KEY = os.getenv(
    "API_KEY",
    ""
)


API_SECRET = os.getenv(
    "API_SECRET",
    "" 
)


RISK_SETTINGS = {
    "max_position_size": 1.0,
    "max_daily_loss": 1000
}


EXECUTION_SETTINGS = {
    "broker": "paper",
    "order_timeout": 30
}
