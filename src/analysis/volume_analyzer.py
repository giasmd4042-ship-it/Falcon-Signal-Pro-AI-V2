"""
Falcon Signal Pro AI V2.0
Volume Analyzer
"""

import pandas as pd


class VolumeAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty or len(data) < 20:
            return "NO DATA"

        volume = data["Volume"]

        if isinstance(volume, pd.DataFrame):
            volume = volume.iloc[:, 0]

        avg_volume = volume.tail(20).mean()
        current_volume = float(volume.iloc[-1])

        if current_volume > avg_volume * 1.5:
            return "HIGH VOLUME"

        elif current_volume < avg_volume * 0.5:
            return "LOW VOLUME"

        return "NORMAL VOLUME"
