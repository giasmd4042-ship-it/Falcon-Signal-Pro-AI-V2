"""
Falcon Signal Pro AI V7
Signal Status Badge
"""

import streamlit as st


def show_status_badge(signal):

    if signal == "BUY":
        st.success("?? BUY SIGNAL")

    elif signal == "SELL":
        st.error("?? SELL SIGNAL")

    else:
        st.warning("?? HOLD SIGNAL")
