"""
Falcon Signal Pro AI V2.0
Application Entry Point
"""

from core.config import (
    APP_NAME,
    VERSION,
    ASSETS,
    TIMEFRAMES,
)

from utils.logger import logger


def main():
    logger.info("Application starting...")

    print("=" * 50)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Assets : {', '.join(ASSETS)}")
    print(f"Timeframes : {', '.join(TIMEFRAMES)}")
    print("=" * 50)

    logger.info("Application started successfully.")


if __name__ == "__main__":
    main()
