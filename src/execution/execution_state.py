import json
import os


class ExecutionState:

    def __init__(self, file_path="execution_state.json"):

        self.file_path = file_path


    def save(self, data):

        with open(self.file_path, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )


    def load(self):

        if not os.path.exists(self.file_path):

            return {}

        with open(self.file_path, "r") as file:

            return json.load(file)


    def clear(self):

        if os.path.exists(self.file_path):

            os.remove(self.file_path)
