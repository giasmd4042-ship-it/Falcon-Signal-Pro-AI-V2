import pandas as pd
import streamlit as st

from src.dashboard.theme import apply_theme
from src.dashboard.sidebar import build_sidebar
from src.dashboard.metrics import show_metrics
from src.dashboard.charts import show_candlestick_chart
from src.dashboard.history import show_trade_history
from src.dashboard.scanner import show_market_scanner
from src.dashboard.ai_card import show_ai_card
from src.dashboard.multi_timeframe_card import show_multi_timeframe
from src.dashboard.status_card import show_status
from src.dashboard.volume_card import show_volume_card

from src.analysis.market_data import MarketData
from src.analysis.signal_generator import SignalGenerator
from src.analysis.support_resistance import SupportResistanceAnalyzer
from src.analysis.candlestick_analyzer import CandlestickAnalyzer
from src.analysis.atr_analyzer import ATRAnalyzer
from src.analysis.take_profit import TakeProfitCalculator
from src.analysis.ai_score_engine import AIScoreEngine
from src.analysis.multi_timeframe import MultiTimeframeAnalyzer

apply_theme()

symbol, timeframe, refresh = build_sidebar()

market = MarketData()
generator = SignalGenerator()
sr = SupportResistanceAnalyzer()
candle = CandlestickAnalyzer()
atr = ATRAnalyzer()
tp = TakeProfitCalculator()
ai = AIScoreEngine()
mtf = MultiTimeframeAnalyzer()

data = market.get_data(symbol=symbol, interval=timeframe)

result = generator.generate(data)
levels = sr.detect(data)
atr_data = atr.detect(data)
pattern = candle.detect(data)

close = data["Close"]

if isinstance(close, pd.DataFrame):
    close = close.iloc[:, 0]

entry = float(close.iloc[-1])

if result["signal"] == "BUY":
    stop = atr_data["buy_sl"]
else:
    stop = atr_data["sell_sl"]

trade = tp.calculate(entry, stop)

mtf_result = mtf.analyze(symbol)
ai_score = ai.calculate(
    result=result,
    pattern=pattern,
    volume=result["volume"]["volume"]
)

st.subheader("Analysis")

st.write("Trend:", result["trend"])
st.write("EMA:", result["ema"])
st.write("RSI:", result["rsi"])
st.write("MACD:", result["macd"])

st.divider()

show_status(result["signal"], result["confidence"])

show_metrics(result, trade)

st.divider()

show_ai_card(ai_score)
show_volume_card(result["volume"])

st.divider()

left, right = st.columns(2)

with left:
    st.metric("Support", f'{levels["support"]:,.2f}')

with right:
    st.metric("Resistance", f'{levels["resistance"]:,.2f}')

st.divider()

show_candlestick_chart(data, symbol)

st.divider()

show_trade_history()

st.divider()

show_market_scanner()

st.divider()
show_multi_timeframe(mtf_result)
st.divider()

st.success("Falcon Signal Pro AI V8 Ready")
