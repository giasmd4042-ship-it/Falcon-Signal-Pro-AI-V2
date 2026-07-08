"""
Falcon Signal Pro AI V8
Professional Dashboard Theme
"""

import streamlit as st


def apply_theme():

    st.set_page_config(
        page_title="Falcon Signal Pro AI V8",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(
        """
        <style>
        .block-container{
            padding-top:1.2rem;
            padding-bottom:1rem;
        }

        div[data-testid="stMetric"]{
            border:1px solid #2b2b2b;
            border-radius:12px;
            padding:12px;
            background:#111827;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Falcon Signal Pro AI Dashboard")
    st.caption("Professional AI Trading Dashboard | Version V8")
