from src.data.market_data_provider_factory import market_data_provider_factory
from src.execution.provider_factory import provider_factory
from src.security.safety_guard import safety_guard


class V339RuntimeProviderValidator:


    def validate(self):

        data_provider = market_data_provider_factory.create()

        broker_provider = provider_factory.create()


        checks = {


            "data_factory":

                data_provider is not None,


            "broker_factory":

                broker_provider is not None,


            "safety_guard":

                safety_guard.allow_trade(),


            "data_mode":

                market_data_provider_factory.mode(),


            "broker_mode":

                provider_factory.mode()

        }


        return {


            "status":

                "PASS"

                if checks["data_factory"]

                and checks["broker_factory"]

                and checks["safety_guard"]

                else "FAIL",



            "checks":

                checks,



            "data_provider":

                type(data_provider).__name__,



            "broker_provider":

                type(broker_provider).__name__,



            "engine":

                "V3.39"

        }



v339_runtime_provider_validator = V339RuntimeProviderValidator()
