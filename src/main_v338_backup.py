"""
Falcon Signal Pro AI V2.0
Production Application Entry Point
"""

from src.core.trading_pipeline import pipeline
from src.monitoring.system_logger import system_logger
from src.monitoring.alert_manager import alert_manager


def main():

    print("=" * 60)
    print("Falcon Signal Pro AI")
    print("Production Trading Engine")
    print("=" * 60)

    system_logger.log("APPLICATION_START")

    alert_manager.send(
        "INFO",
        "Application Started"
    )

    try:

        result = pipeline.run()

        print("\nTRADING RESULT")
        print("=" * 60)

        print("Signal:")
        print(result.get("signal"))

        print("\nOrder:")
        print(result.get("order"))

        print("\nPosition:")
        print(result.get("position"))

        print("\nAnalytics:")
        print(result.get("analytics"))

        print("=" * 60)

        system_logger.log(
            "APPLICATION_COMPLETED",
            result
        )


    except Exception as error:

        system_logger.log(
            "APPLICATION_ERROR",
            {"error": str(error)}
        )

        alert_manager.send(
            "ERROR",
            "Application Failed",
            {"error": str(error)}
        )

        print("ERROR:", error)



if __name__ == "__main__":
    main()
