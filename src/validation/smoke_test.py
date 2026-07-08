from src.core.trading_pipeline import pipeline
from src.dashboard.dashboard_service import dashboard
from src.core.logger import logger

from src.validation.v335_validator import v335_validator


class SmokeTest:


    def run(self):

        result = {}


        try:

            pipeline_result = pipeline.run()

            result["pipeline"] = "PASS"
            result["signal"] = pipeline_result.get("signal")


        except Exception as e:

            result["pipeline"] = "FAIL"
            result["pipeline_error"] = str(e)



        try:

            status = dashboard.status()

            result["dashboard"] = "PASS"
            result["dashboard_status"] = status


        except Exception as e:

            result["dashboard"] = "FAIL"
            result["dashboard_error"] = str(e)



        try:

            logger.info("V3.35 Smoke Test")

            result["logger"] = "PASS"


        except Exception as e:

            result["logger"] = "FAIL"
            result["logger_error"] = str(e)



        try:

            runtime = v335_validator.validate()

            result["runtime_validation"] = runtime


        except Exception as e:

            result["runtime_validation"] = {
                "status": "FAIL",
                "error": str(e)
            }



        result["overall"] = (
            "PASS"
            if
            result.get("pipeline") == "PASS"
            and result.get("dashboard") == "PASS"
            and result.get("logger") == "PASS"
            and result["runtime_validation"].get("status") == "PASS"
            else "FAIL"
        )


        result["engine"] = "V3.35"


        return result



smoke_test = SmokeTest()
