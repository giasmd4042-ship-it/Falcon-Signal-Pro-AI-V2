"""
Falcon Signal Pro AI V11.2
Risk Reward Card
"""

import streamlit as st


def show_risk_reward_card(rr):

    st.subheader("Risk / Reward Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Risk", rr["risk"])
        st.metric("Reward", rr["reward"])

    with col2:
        st.metric("Ratio", f'1 : {rr["ratio"]}')
        st.metric("Quality", rr["quality"])

    if rr["quality"] == "EXCELLENT":
        st.success("????? Excellent Trade")

    elif rr["quality"] == "GOOD":
        st.success("???? Good Trade")

    elif rr["quality"] == "AVERAGE":
        st.warning("??? Average Trade")

    else:
        st.error("?? Poor Trade")
