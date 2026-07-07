"""
Falcon Signal Pro AI V7
Status Bar
"""

from datetime import datetime
import streamlit as st


def show_status_bar():

    st.caption(
        f"?? Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
