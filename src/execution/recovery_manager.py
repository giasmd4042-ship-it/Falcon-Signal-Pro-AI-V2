from src.execution.execution_state import ExecutionState


class RecoveryManager:

    def __init__(self, state_manager):

        self.state_manager = state_manager


    def restore(self):

        state = self.state_manager.load()

        return state


    def has_recovery_data(self):

        state = self.state_manager.load()

        return bool(state)


    def clear_recovery(self):

        self.state_manager.clear()
