import streamlit as st
import json

from src.core.trading_pipeline import pipeline
from src.dashboard.dashboard_service import dashboard
from src.dashboard.dashboard_state import dashboard_state


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
st.subheader("Production Trading Dashboard V3.47")


if st.button("Run Trading Pipeline"):

    result = pipeline.run()

    dashboard.update(result)

    dashboard_state.update(result)

    st.success(
        "Pipeline Executed Successfully"
    )


status = dashboard.status()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "System",
        status["system"]
    )


with col2:
    st.metric(
        "Pipeline",
        status["pipeline"]
    )


with col3:
    st.metric(
        "Execution",
        status["engine_health"]["execution"]
    )


with col4:
    st.metric(
        "Dashboard",
        status["engine_health"]["dashboard"]
    )


st.divider()


st.header("Signal")

st.json(
    safe_json(
        status.get("signal")
    )
)


st.header("Positions")

st.json(
    safe_json(
        status.get("positions")
    )
)


st.header("Orders")

st.json(
    safe_json(
        status.get("orders")
    )
)


st.header("Performance")

st.json(
    safe_json(
        status.get("performance")
    )
)


st.header("Alerts")

st.json(
    safe_json(
        status.get("alerts")
    )
)


st.divider()

st.caption(
    "Falcon Signal Pro AI Engine V3.47 - Live Dashboard State Enabled"
)