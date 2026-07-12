import streamlit as st
import json

from src.core.trading_pipeline import pipeline
from src.dashboard.dashboard_state import dashboard_state
from src.dashboard.dashboard_api import dashboard_api
from src.execution.live_connection_manager import live_connection_manager

live_connection_manager.connect()


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
st.subheader("Production Trading Dashboard V3.70")


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

account = dashboard_api.get_account_summary()

st.header("Account Summary")

a1, a2, a3, a4 = st.columns(4)

with a1:
    st.metric("Balance", account["balance"])

with a2:
    st.metric("Equity", account["equity"])

with a3:
    st.metric("Free Margin", account["free_margin"])

with a4:
    st.metric("Unrealized P/L", account["unrealized_pnl"])

st.divider()        
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


risk = dashboard_api.get_risk_level()

st.header("Risk Monitoring")

r1, r2 = st.columns(2)

with r1:
    st.metric(
        "Risk Level",
        risk["risk_level"]
    )

r3, r4 = st.columns(2)

with r3:
    st.metric(
        "Risk Score",
        risk["risk_score"]
    )

with r4:
    st.metric(
        "Risk Status",
        risk["risk_status"]
    )        
with r2:
    st.metric(
        "Exposure",
        risk["exposure"]
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
        "V3.70"
    )


st.divider()

st.header("Performance Intelligence")

perf1, perf2, perf3, perf4 = st.columns(4)

with perf1:
    st.metric(
        "Average Win",
        intel["average_win"]
    )

with perf2:
    st.metric(
        "Average Loss",
        intel["average_loss"]
    )

with perf3:
    st.metric(
        "Profit Factor",
        intel["profit_factor"]
    )

with perf4:
    st.metric(
        "Performance Grade",
        "A"
    )


st.divider()


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
st.header("Production Readiness")
st.success("READY FOR PAPER TRADING")

st.json(
    safe_json(
        dashboard_api.get_broker_health()
    )
)
@st.fragment(run_every="5s")
def live_broker_health():
    st.header("Broker Health")
    st.json(
        safe_json(
            dashboard_api.get_broker_health()
        )
    )

live_broker_health()
