"""
Falcon Signal Pro AI V2
Dashboard Theme
"""

import streamlit as st

def apply_theme():
    st.set_page_config(
        page_title="Falcon Signal Pro AI",
        page_icon="??",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("?? Falcon Signal Pro AI Dashboard")
    st.caption("Professional Trading Dashboard")
