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
st.subheader("Production Trading Dashboard V3.50")


if st.button("Run Trading Pipeline"):

    result = pipeline.run()

    dashboard_state.update(result)

    st.success(
        "Pipeline Executed Successfully"
    )


if dashboard_api.get_signal() is None:

    result = pipeline.run()

    dashboard_state.update(result)


health = dashboard_api.get_health()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric("System", health["system"])


with col2:
    st.metric("Pipeline", health["pipeline"])


with col3:
    st.metric(
        "Execution",
        health["engine_health"]["execution"]
    )


with col4:
    st.metric(
        "Dashboard",
        health["engine_health"]["dashboard"]
    )


st.divider()


col1, col2 = st.columns(2)


with col1:
    st.header("Signal")
    st.json(
        safe_json(
            dashboard_api.get_signal()
        )
    )


with col2:
    st.header("Risk Snapshot")
    st.json(
        safe_json(
            dashboard_api.get_risk_snapshot()
        )
    )


st.divider()


col1, col2 = st.columns(2)


with col1:
    st.header("Signal History")
    st.json(
        safe_json(
            dashboard_api.get_signal_history()
        )
    )


with col2:
    st.header("Trade History")
    st.json(
        safe_json(
            dashboard_api.get_trade_history()
        )
    )


st.divider()


st.header("Performance")

st.json(
    safe_json(
        dashboard_api.get_performance()
    )
)
