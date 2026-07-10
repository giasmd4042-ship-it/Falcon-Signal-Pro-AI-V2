"""
Falcon Signal Pro AI V8.1
Professional Signal Status Card
"""

import streamlit as st


def show_status(signal, confidence):

    if signal == "BUY":
        st.success(f"?? BUY SIGNAL | Confidence: {confidence}%")

    elif signal == "SELL":
        st.error(f"?? SELL SIGNAL | Confidence: {confidence}%")

    else:
        st.warning(f"?? HOLD | Confidence: {confidence}%")
