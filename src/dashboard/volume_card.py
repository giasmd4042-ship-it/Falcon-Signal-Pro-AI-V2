"""
Falcon Signal Pro AI V10.3
Volume Analysis Card
"""

import streamlit as st


def show_volume_card(volume):

    st.subheader("Volume Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Status",
            volume.get("volume", "UNKNOWN")
        )

    with col2:
        st.metric(
            "Ratio",
            f'{volume.get("ratio", 0)}x'
        )

    with col3:
        st.metric(
            "Strength",
            f'{volume.get("strength", 0)}%'
        )

    if volume.get("volume") == "HIGH VOLUME":
        st.success("Strong Volume Confirmation")

    elif volume.get("volume") == "LOW VOLUME":
        st.warning("Weak Volume")

    else:
        st.info("Normal Volume")
