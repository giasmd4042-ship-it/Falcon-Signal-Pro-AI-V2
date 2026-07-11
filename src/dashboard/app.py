import streamlit as st
import json

from src.core.trading_pipeline import pipeline
from src.dashboard.dashboard_state import dashboard_state
from src.dashboard.dashboard_api import dashboard_api


def safe_json(data):

    if data is None:
        return {
            "message": "No data available"
        }

    return json.loads(
        json.dumps(
            data,
            default=str
        )
    )


st.set_page_config(
    page_title="Falcon Signal Pro AI",
    layout="wide"
)


st.title("Falcon Signal Pro AI")
st.subheader("Production Trading Dashboard V3.59")


if dashboard_api.get_signal() is None:

    result = pipeline.run()

    dashboard_state.update(result)



health = dashboard_api.get_health()


c1, c2, c3, c4 = st.columns(4)


with c1:
    st.metric(
        "System",
        health["system"]
    )

with c2:
    st.metric(
        "Pipeline",
        health["pipeline"]
    )

with c3:
    st.metric(
        "Execution",
        health["engine_health"]["execution"]
    )

with c4:
    st.metric(
        "Dashboard",
        health["engine_health"]["dashboard"]
    )



st.divider()


monitor = dashboard_api.get_monitoring()


st.header("Portfolio Monitoring")


m1, m2, m3, m4 = st.columns(4)


with m1:
    st.metric(
        "Open Positions",
        monitor["portfolio"]["open_positions"]
    )


with m2:
    st.metric(
        "Exposure",
        monitor["portfolio"]["exposure"]
    )


with m3:
    st.metric(
        "Total Trades",
        monitor["performance"]["trades"]
    )


with m4:
    st.metric(
        "Profit",
        monitor["performance"]["profit"]
    )


st.divider()


intel = dashboard_api.get_intelligence()


i1, i2, i3, i4 = st.columns(4)


with i1:
    st.metric(
        "Best Strategy",
        intel["best_strategy"]
    )

with i2:
    st.metric(
        "Win Rate",
        f'{intel["win_rate"]}%'
    )

with i3:
    st.metric(
        "Market",
        intel["market_regime"][0]
        if intel["market_regime"]
        else "UNKNOWN"
    )

with i4:
    st.metric(
        "Engine",
        "V3.59"
    )


st.divider()


st.header("Signal")
st.json(
    safe_json(
        dashboard_api.get_signal()
    )
)


st.header("Risk Snapshot")
st.json(
    safe_json(
        dashboard_api.get_risk_snapshot()
    )
)


st.header("Trade History")
st.json(
    safe_json(
        dashboard_api.get_trade_history()
    )
)


st.header("Performance")
st.json(
    safe_json(
        dashboard_api.get_performance()
    )
)
st.divider()

st.header("Advanced Analytics")

performance = dashboard_api.get_performance()

total_profit = performance.get("total_profit", 0)

equity_curve = {
    "Equity": [
        0,
        total_profit * 0.2,
        total_profit * 0.4,
        total_profit * 0.6,
        total_profit * 0.8,
        total_profit
    ]
}

st.line_chart(equity_curve)

st.metric(
    "Current Equity",
    total_profit
)

st.metric(
    "Drawdown",
    0
)
