"""
Falcon Signal Pro AI V7
Live Price Card
"""

import streamlit as st


def show_price_card(symbol, price):

    st.subheader("?? Live Market")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Symbol",
            symbol
        )

    with col2:
        st.metric(
            "Current Price",
            f"{price:,.2f}"
        )
