"""
Falcon Signal Pro AI V10.6
Breakout Analysis Card
"""

import streamlit as st


def show_breakout_card(breakout):

    st.subheader("Breakout Analysis")

    if breakout == "BULLISH BREAKOUT":
        st.success("🚀 Bullish Breakout Confirmed")

    elif breakout == "BEARISH BREAKOUT":
        st.error("🔻 Bearish Breakout Confirmed")

    elif breakout == "NO BREAKOUT":
        st.info("➖ No Breakout")

    else:
        st.warning(str(breakout))
