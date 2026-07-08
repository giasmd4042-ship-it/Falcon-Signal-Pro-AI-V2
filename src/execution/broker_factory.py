from src.core.config import BROKER_MODE

from src.execution.paper_broker import PaperBroker
from src.execution.live_broker import LiveBroker


class BrokerFactory:


    def create(self):

        if BROKER_MODE == "live":

            broker = LiveBroker()

            if broker.connect():

                return broker


            return PaperBroker()


        return PaperBroker()



    def mode(self):

        return BROKER_MODE



broker_factory = BrokerFactory()
