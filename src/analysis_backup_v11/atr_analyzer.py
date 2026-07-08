"""
Falcon Signal Pro AI V2.0
ATR Analyzer
"""

import pandas as pd


class ATRAnalyzer:

    def detect(self, data: pd.DataFrame):

        if data.empty or len(data) < 15:
            return None

        def series(col):
            s = data[col]
            if isinstance(s, pd.DataFrame):
                s = s.iloc[:, 0]
            return s

        high = series("High")
        low = series("Low")
        close = series("Close")

        tr1 = high - low
        tr2 = (high - close.shift()).abs()
        tr3 = (low - close.shift()).abs()

        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

        atr = tr.rolling(14).mean()

        last_close = float(close.iloc[-1])
        last_atr = float(atr.iloc[-1])

        stop_loss_buy = round(last_close - (last_atr * 1.5), 2)
        stop_loss_sell = round(last_close + (last_atr * 1.5), 2)

        return {
            "atr": round(last_atr, 2),
            "buy_sl": stop_loss_buy,
            "sell_sl": stop_loss_sell
        }

