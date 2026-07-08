"""
Falcon Signal Pro AI V9
Multi Timeframe Card
"""

import streamlit as st


def show_multi_timeframe(result):

    st.subheader("Multi-Timeframe Analysis")

    cols = st.columns(5)

    frames = ["15m", "1h", "4h", "1d", "overall"]

    for col, tf in zip(cols, frames):

        with col:
            value = result.get(tf, "-")

            if value == "BULLISH":
                st.success(f"{tf}\n\n🟢 {value}")

            elif value == "BEARISH":
                st.error(f"{tf}\n\n🔴 {value}")

            elif value == "NEUTRAL":
                st.warning(f"{tf}\n\n🟡 {value}")

            else:
                st.info(f"{tf}\n\n⚪ {value}")
