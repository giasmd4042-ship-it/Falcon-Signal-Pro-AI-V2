"""
Falcon Signal Pro AI V11
Risk Card
"""

import streamlit as st


def show_risk_card(risk):

    st.subheader("Smart Risk Management")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Account Balance", f'${risk["balance"]:,.2f}')
        st.metric("Risk", f'{risk["risk_percent"]}%')
        st.metric("Risk Amount", f'${risk["risk_amount"]:,.2f}')

    with col2:
        st.metric("Position Size", risk["position_size"])
        st.metric("Stop Distance", risk["stop_distance"])

    if risk["position_size"] > 0:
        st.success("Position sizing calculated successfully.")
    else:
        st.warning("Invalid stop loss distance.")
