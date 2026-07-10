from datetime import datetime

from src.core.trading_pipeline import pipeline
from src.dashboard.monitoring_dashboard import monitoring_dashboard
from src.core.logger import logger


class SmokeTest:

    def run(self):

        results = {}

        try:
            pipeline_result = pipeline.run()
            results["pipeline"] = "PASS"
            results["signal"] = pipeline_result.get("signal", {})
        except Exception as e:
            results["pipeline"] = "FAIL"
            results["pipeline_error"] = str(e)

        try:
            dashboard_result = monitoring_dashboard.view()
            results["dashboard"] = "PASS"
            results["dashboard_status"] = dashboard_result.get("status", {})
        except Exception as e:
            results["dashboard"] = "FAIL"
            results["dashboard_error"] = str(e)

        try:
            logger.info("V3.33 Smoke Test Completed")
            results["logger"] = "PASS"
        except Exception as e:
            results["logger"] = "FAIL"
            results["logger_error"] = str(e)

        results["overall"] = (
            "PASS"
            if all(
                results.get(x) == "PASS"
                for x in ["pipeline", "dashboard", "logger"]
            )
            else "FAIL"
        )

        results["timestamp"] = datetime.now(datetime.UTC).isoformat()
        results["engine"] = "V3.33"

        return results


smoke_test = SmokeTest()
