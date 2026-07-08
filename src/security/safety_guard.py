class SafetyGuard:


    def __init__(self):

        self.enabled = True


    def allow_trade(self):

        return self.enabled


    def emergency_stop(self):

        self.enabled = False
        return True


    def resume(self):

        self.enabled = True
        return True



safety_guard = SafetyGuard()
