"""
Falcon Signal Pro AI V11.3
Volatility Card
"""

import streamlit as st


def show_volatility_card(volatility):

    st.subheader("Volatility Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATR", volatility["atr"])

    with col2:
        st.metric("Level", volatility["level"])

    with col3:
        st.metric("Risk", volatility["risk"])

    if volatility["level"] == "LOW":
        st.success("🟢 Low Volatility")

    elif volatility["level"] == "MEDIUM":
        st.warning("🟡 Medium Volatility")

    elif volatility["level"] == "HIGH":
        st.error("🔴 High Volatility")

    else:
        st.info("Volatility Unknown")
