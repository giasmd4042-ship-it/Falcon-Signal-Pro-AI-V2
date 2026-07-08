class ExecutionRiskGuard:

    def __init__(
        self,
        max_position_size=1.0,
        max_daily_loss=1000
    ):

        self.max_position_size = max_position_size
        self.max_daily_loss = max_daily_loss


    def check_quantity(self, quantity):

        return quantity <= self.max_position_size


    def check_balance(self, balance, required):

        return balance >= required


    def check_daily_loss(self, loss):

        return loss <= self.max_daily_loss


    def approve(
        self,
        quantity,
        balance,
        required,
        daily_loss=0
    ):

        if not self.check_quantity(quantity):
            return False

        if not self.check_balance(balance, required):
            return False

        if not self.check_daily_loss(daily_loss):
            return False

        return True
