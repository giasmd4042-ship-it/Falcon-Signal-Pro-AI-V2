"""
Falcon Signal Pro AI V10
Smart Volume Analyzer
"""

import pandas as pd


class VolumeAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty or "Volume" not in data.columns:
            return {
                "volume": "UNKNOWN",
                "ratio": 0,
                "strength": 0
            }

        volume = data["Volume"]

        if isinstance(volume, pd.DataFrame):
            volume = volume.iloc[:, 0]

        avg_volume = volume.rolling(20).mean().iloc[-1]
        current_volume = volume.iloc[-1]

        if avg_volume == 0 or pd.isna(avg_volume):
            ratio = 0
        else:
            ratio = round(float(current_volume / avg_volume), 2)

        if ratio >= 1.5:
            status = "HIGH VOLUME"
            strength = 100

        elif ratio >= 0.8:
            status = "NORMAL VOLUME"
            strength = 60

        else:
            status = "LOW VOLUME"
            strength = 30

        return {
            "volume": status,
            "ratio": ratio,
            "strength": strength
        }
