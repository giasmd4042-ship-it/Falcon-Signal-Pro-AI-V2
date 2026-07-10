import streamlit as st
import json

from src.core.trading_pipeline import pipeline


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
st.subheader("Production Trading Dashboard V3.43")


if "result" not in st.session_state:

    st.session_state.result = None



if st.button("Run Trading Pipeline"):

    st.session_state.result = pipeline.run()

    st.success(
        "Pipeline Executed Successfully"
    )



result = st.session_state.result



if result:


    signal = result.get("signal")

    positions = result.get("position")

    order = result.get("order")

    analytics = result.get("analytics")


    status_system = "ONLINE"

else:

    signal = None
    positions = []
    order = None
    analytics = {}

    status_system = "ONLINE"



col1,col2,col3,col4 = st.columns(4)


with col1:
    st.metric(
        "System",
        status_system
    )


with col2:
    st.metric(
        "Pipeline",
        "RUNNING"
    )


with col3:
    st.metric(
        "Execution",
        "OK"
    )


with col4:
    st.metric(
        "Dashboard",
        "OK"
    )



st.divider()


st.header("Signal")

st.json(
    safe_json(signal)
)



st.header("Positions")

st.json(
    safe_json(positions)
)



st.header("Orders")

st.json(
    safe_json(order)
)



st.header("Performance")

st.json(
    safe_json(analytics)
)

