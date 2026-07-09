from src.data.live_market_data_adapter import live_market_data_adapter
from src.execution.broker_api_client import broker_api_client
from src.execution.broker_order_gateway import BrokerOrderGateway
from src.security.safety_guard import safety_guard


class V337RuntimeValidator:


    def validate(self):

        data_ok = live_market_data_adapter.connect()

        broker_ok = broker_api_client.connect()


        gateway = BrokerOrderGateway(
            broker_api_client
        )


        order_result = gateway.submit_order(
            {
                "symbol": "BTCUSDT",
                "side": "BUY",
                "quantity": 1
            }
        )


        checks = {

            "market_data":
                data_ok,

            "broker_connection":
                broker_ok,

            "safety_layer":
                safety_guard.allow_trade(),

            "order_gateway":
                order_result["status"] != "SUBMITTED"

        }


        return {

            "status":
                "PASS" if all(checks.values()) else "BLOCKED",

            "checks":
                checks,

            "order_test":
                order_result,

            "engine":
                "V3.37"

        }



v337_runtime_validator = V337RuntimeValidator()
