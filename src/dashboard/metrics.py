"""
Falcon Signal Pro AI V2
Dashboard Metrics
"""

import streamlit as st

def show_metrics(result, trade):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Signal", result["signal"])

    with col2:
        st.metric("Confidence", f'{result["confidence"]}%')

    with col3:
        st.metric("Entry", f'{trade["entry"]:,.2f}')

    with col4:
        st.metric("Take Profit", f'{trade["take_profit"]:,.2f}')

    col5, col6 = st.columns(2)

    with col5:
        st.metric("Stop Loss", f'{trade["stop_loss"]:,.2f}')

    with col6:
        st.metric("Trend", result["trend"])
