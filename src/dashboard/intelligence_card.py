import streamlit as st


def show_intelligence_card(intelligence):

    if not intelligence:
        return

    decision = intelligence.get("decision", {})
    reasoning = intelligence.get("reasoning", {})

    st.subheader("🧠 Falcon Intelligence Layer")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "AI Decision",
            decision.get("decision", "WAIT")
        )

    with col2:
        st.metric(
            "Confidence",
            f"{decision.get('confidence', 0)}%"
        )

    with col3:
        st.metric(
            "Engine",
            intelligence.get("engine", "V3.25.0")
        )

    st.info(
        reasoning.get(
            "reasoning",
            "No reasoning available"
        )
    )
