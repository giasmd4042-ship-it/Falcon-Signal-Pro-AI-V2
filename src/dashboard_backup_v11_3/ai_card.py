"""
Falcon Signal Pro AI V2
AI Score Card
"""

import streamlit as st


def show_ai_card(score):

    st.subheader("AI Score")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "AI Score",
            f'{score["percent"]}%'
        )

    with col2:
        st.metric(
            "Grade",
            score["grade"]
        )

    with col3:
        st.metric(
            "Raw Score",
            f'{score["score"]}/{score["max_score"]}'
        )

    st.progress(score["percent"] / 100)

    if score["grade"] == "A+":
        st.success("Excellent Trade Setup")

    elif score["grade"] == "A":
        st.success("Strong Trade Setup")

    elif score["grade"] == "B":
        st.warning("Average Trade Setup")

    else:
        st.error("Weak Trade Setup")
