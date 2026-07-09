import os


class ProductionEnvironment:


    def __init__(self):

        self.environment = os.getenv(
            "APP_ENV",
            "development"
        )



    def is_production(self):

        return self.environment == "production"



    def get_environment(self):

        return self.environment



    def allow_live(self):

        return self.is_production()



production_environment = ProductionEnvironment()
