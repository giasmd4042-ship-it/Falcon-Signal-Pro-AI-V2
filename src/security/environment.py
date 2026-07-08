import os


class EnvironmentManager:


    def get_environment(self):

        return os.getenv(
            "FALCON_ENV",
            "development"
        )


    def is_production(self):

        return self.get_environment() == "production"



environment = EnvironmentManager()
