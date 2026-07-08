"""
Falcon Signal Pro AI V2
Dashboard Charts
"""

import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def show_candlestick_chart(data: pd.DataFrame, symbol: str):

    chart = data.copy()

    for col in ["Open", "High", "Low", "Close"]:
        if isinstance(chart[col], pd.DataFrame):
            chart[col] = chart[col].iloc[:, 0]

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=chart.index,
            open=chart["Open"],
            high=chart["High"],
            low=chart["Low"],
            close=chart["Close"],
            name=symbol
        )
    )

    fig.update_layout(
        title=f"{symbol} Candlestick Chart",
        height=600,
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig, width="stretch")
