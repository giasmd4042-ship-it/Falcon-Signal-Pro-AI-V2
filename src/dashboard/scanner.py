"""
Falcon Signal Pro AI V2
Multi Symbol Scanner
"""

import pandas as pd
import streamlit as st

from src.analysis.market_data import MarketData
from src.analysis.signal_generator import SignalGenerator


def show_market_scanner():

    st.subheader("Market Scanner")

    market = MarketData()
    generator = SignalGenerator()

    symbols = [
        "BTC-USD",
        "ETH-USD",
        "GC=F",
        "SI=F"
    ]

    rows = []

    for symbol in symbols:

        try:
            data = market.get_data(symbol)
            result = generator.generate(data)

            rows.append({
                "Symbol": symbol,
                "Signal": result["signal"],
                "Trend": result["trend"],
                "Confidence": f'{result["confidence"]}%'
            })

        except Exception as e:

            rows.append({
                "Symbol": symbol,
                "Signal": "ERROR",
                "Trend": "-",
                "Confidence": str(e)
            })

    df = pd.DataFrame(rows)

    st.dataframe(df, width="stretch", hide_index=True)
