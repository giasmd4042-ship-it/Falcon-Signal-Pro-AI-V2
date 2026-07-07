"""
Falcon Signal Pro AI V2
Dashboard Sidebar
"""

import streamlit as st

def build_sidebar():

    st.sidebar.header("Settings")

    symbol = st.sidebar.selectbox(
        "Select Symbol",
        [
            "BTC-USD",
            "ETH-USD",
            "GC=F",
            "SI=F"
        ]
    )

    timeframe = st.sidebar.selectbox(
        "Timeframe",
        [
            "15m",
            "1h",
            "4h",
            "1d"
        ]
    )

    refresh = st.sidebar.button("Refresh Data")

    return symbol, timeframe, refresh
