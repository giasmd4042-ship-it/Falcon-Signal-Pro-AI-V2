from src.execution.execution_state import ExecutionState


class FailoverManager:

    def __init__(self, state_manager):

        self.state_manager = state_manager
        self.failed = False


    def trigger_failover(self, state):

        self.state_manager.save(state)

        self.failed = True

        return True


    def is_failed(self):

        return self.failed


    def recover_state(self):

        return self.state_manager.load()
