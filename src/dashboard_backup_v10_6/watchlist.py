"""
Falcon Signal Pro AI V7.3
Smart Watchlist
"""

import streamlit as st


def show_watchlist():

    st.subheader("?? Smart Watchlist")

    symbols = [
        "BTC-USD",
        "ETH-USD",
        "GC=F",
        "SI=F",
        "EURUSD=X",
        "GBPUSD=X"
    ]

    for symbol in symbols:
        st.write(f"• {symbol}")

