"""
Falcon Signal Pro AI V2.0
Trade Logger
"""

import csv
import os
from datetime import datetime


class TradeLogger:

    def __init__(self, filename="trade_log.csv"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Time",
                    "Symbol",
                    "Signal",
                    "Entry",
                    "StopLoss",
                    "TakeProfit",
                    "Confidence",
                    "AI_Score",
                    "Grade"
                ])

    def log(self, plan):

        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                plan["symbol"],
                plan["signal"],
                plan["entry"],
                plan["stop_loss"],
                plan["take_profit"],
                plan["confidence"],
                plan["ai_score"],
                plan["grade"]
            ])

        return "Trade Saved"
