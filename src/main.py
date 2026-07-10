"""
Falcon Signal Pro AI
Production Trading Engine
V3.38 Dashboard Integration
"""

from src.core.trading_pipeline import pipeline
from src.dashboard.dashboard_service import dashboard


def main():

    print("=" * 60)
    print("Falcon Signal Pro AI")
    print("Production Trading Engine")
    print("=" * 60)


    result = pipeline.run()


    dashboard.update(result)


    print("\nTRADING RESULT")
    print("=" * 60)

    print("\nSignal:")
    print(result.get("signal"))


    print("\nOrder:")
    print(result.get("order"))


    print("\nPosition:")
    print(result.get("position"))


    print("\nAnalytics:")
    print(result.get("analytics"))


    print("=" * 60)



if __name__ == "__main__":
    main()
