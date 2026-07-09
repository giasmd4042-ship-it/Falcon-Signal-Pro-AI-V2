from src.core.config import BROKER_MODE

from src.execution.paper_broker import PaperBroker
from src.execution.real_provider import RealProviderInterface



class ProviderFactory:


    def create(self):


        if BROKER_MODE == "live":

            return RealProviderInterface()


        return PaperBroker()



    def mode(self):

        return BROKER_MODE




provider_factory = ProviderFactory()
