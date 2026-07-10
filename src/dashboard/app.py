import streamlit as st
import json
import pandas as pd

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
st.subheader("Production Trading Dashboard V3.52")


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


c1, c2, c3, c4 = st.columns(4)


with c1:
    st.metric("System", health["system"])

with c2:
    st.metric("Pipeline", health["pipeline"])

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
        "Profit",
        intel["total_profit"]
    )

with i4:
    st.metric(
        "Market",
        intel["market_regime"][0]
        if intel["market_regime"]
        else "UNKNOWN"
    )


st.divider()


charts = dashboard_api.get_chart_data()


st.header("Strategy Performance")


strategy_df = pd.DataFrame(
    charts["strategy_performance"]
)

if not strategy_df.empty:
    st.bar_chart(
        strategy_df.set_index(
            "strategy"
        )["profit"]
    )


st.header("Win / Loss")


wl_df = pd.DataFrame(
    [
        {
            "Result": "Wins",
            "Count": charts["win_loss"]["wins"]
        },
        {
            "Result": "Losses",
            "Count": charts["win_loss"]["losses"]
        }
    ]
)


st.bar_chart(
    wl_df.set_index(
        "Result"
    )
)


st.header("Profit Curve")


profit_df = pd.DataFrame(
    charts["profit_curve"]
)


if not profit_df.empty:

    st.line_chart(
        profit_df.set_index(
            "trade"
        )["profit"]
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


st.header("Signal History")
st.json(
    safe_json(
        dashboard_api.get_signal_history()
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
