from datetime import datetime


class ExecutionMetrics:

    def __init__(self):

        self.total_orders = 0
        self.successful_orders = 0
        self.failed_orders = 0
        self.start_time = datetime.now(datetime.UTC)


    def record_success(self):

        self.total_orders += 1
        self.successful_orders += 1


    def record_failure(self):

        self.total_orders += 1
        self.failed_orders += 1


    def report(self):

        success_rate = 0

        if self.total_orders:
            success_rate = (
                self.successful_orders /
                self.total_orders
            ) * 100


        return {
            "total_orders": self.total_orders,
            "successful_orders": self.successful_orders,
            "failed_orders": self.failed_orders,
            "success_rate": success_rate,
            "started": self.start_time.isoformat(),
            "timestamp": datetime.now(datetime.UTC).isoformat()
        }


execution_metrics = ExecutionMetrics()
