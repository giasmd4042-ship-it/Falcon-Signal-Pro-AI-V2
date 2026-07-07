"""
Falcon Signal Pro AI V2
Trade History
"""

from pathlib import Path

import pandas as pd
import streamlit as st


def show_trade_history():

    log_file = Path("trade_log.csv")

    if not log_file.exists():
        st.info("No trade history available.")
        return

    df = pd.read_csv(log_file)

    st.subheader("Trade History")

    st.dataframe(df, width="stretch")
