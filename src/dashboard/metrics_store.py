import json
from pathlib import Path
from datetime import datetime, timezone


class MetricsStore:

    def __init__(self):
        self.path = Path("metrics_store.json")


    def save(self, metrics):

        payload = {
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "metrics": metrics
        }

        self.path.write_text(
            json.dumps(
                payload,
                indent=4
            ),
            encoding="utf-8"
        )

        return True


    def load(self):

        if not self.path.exists():
            return {}

        return json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )


metrics_store = MetricsStore()