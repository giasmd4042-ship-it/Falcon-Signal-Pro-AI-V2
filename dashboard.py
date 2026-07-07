import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from src.analysis.market_data import MarketData
from src.analysis.signal_generator import SignalGenerator
from src.analysis.support_resistance import SupportResistanceAnalyzer
from src.analysis.candlestick_analyzer import CandlestickAnalyzer
from src.analysis.atr_analyzer import ATRAnalyzer
from src.analysis.take_profit import TakeProfitCalculator

st.set_page_config(
    page_title="Falcon Signal Pro AI V2",
    page_icon="??",
    layout="wide"
)

st.title("?? Falcon Signal Pro AI V2")

symbol = st.selectbox(
    "Market",
    ["BTC-USD", "GC=F"]
)

market = MarketData()
generator = SignalGenerator()
sr = SupportResistanceAnalyzer()
candle = CandlestickAnalyzer()
atr = ATRAnalyzer()
tp = TakeProfitCalculator()

data = market.get_data(symbol)

result = generator.generate(data)
levels = sr.detect(data)
pattern = candle.detect(data)
atr_data = atr.detect(data)

close = data["Close"]
if isinstance(close, pd.DataFrame):
    close = close.iloc[:, 0]

entry = float(close.iloc[-1])

if result["signal"] == "BUY":
    stop = atr_data["buy_sl"]
else:
    stop = atr_data["sell_sl"]

trade = tp.calculate(entry, stop)

left, right = st.columns(2)

with left:
    st.subheader("Analysis")
    st.write("Trend:", result["trend"])
    st.write("EMA:", result["ema"])
    st.write("RSI:", result["rsi"])
    st.write("MACD:", result["macd"])
    st.write("Pattern:", pattern)

with right:
    st.subheader("Trade")
    st.metric("Signal", result["signal"])
    st.metric("Confidence", f"{result['confidence']}%")
    st.metric("Entry", trade["entry"])
    st.metric("Stop Loss", trade["stop_loss"])
    st.metric("Take Profit", trade["take_profit"])

st.divider()

st.subheader("Support / Resistance")

c1, c2 = st.columns(2)

with c1:
    st.metric("Support", levels["support"])

with c2:
    st.metric("Resistance", levels["resistance"])

st.divider()

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
        name="Price"
    )
)

fig.update_layout(
    title=f"{symbol} Chart",
    height=600,
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, width="stretch")

st.divider()

st.subheader("Trade History")

try:
    history = pd.read_csv("trade_log.csv")
    st.dataframe(history, width="stretch")
except FileNotFoundError:
    st.info("No trade history available.")
