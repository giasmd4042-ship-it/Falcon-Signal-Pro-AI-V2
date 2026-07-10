import streamlit as st

from src.core.trading_pipeline import pipeline
from src.dashboard.dashboard_service import dashboard


st.set_page_config(
    page_title="Falcon Signal Pro AI",
    layout="wide"
)


st.title("?? Falcon Signal Pro AI")
st.subheader("Production Trading Dashboard V3.39")


if st.button("Run Trading Pipeline"):

    result = pipeline.run()

    dashboard.update(result)

    st.success("Pipeline Executed")


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
    status.get("signal")
)


st.header("Positions")

st.write(
    status.get("positions")
)


st.header("Orders")

st.write(
    status.get("orders")
)


st.header("Performance")

st.json(
    status.get("performance")
)


st.header("Alerts")

st.write(
    status.get("alerts")
)
