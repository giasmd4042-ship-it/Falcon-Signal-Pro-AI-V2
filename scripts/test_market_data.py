from src.analysis.market_data import MarketData
from src.analysis.trend_analyzer import TrendAnalyzer
from src.analysis.ema_analyzer import EMAAnalyzer
from src.analysis.rsi_analyzer import RSIAnalyzer
from src.analysis.macd_analyzer import MACDAnalyzer
from src.analysis.support_resistance import SupportResistanceAnalyzer
from src.analysis.candlestick_analyzer import CandlestickAnalyzer
from src.analysis.signal_generator import SignalGenerator
from src.analysis.atr_analyzer import ATRAnalyzer
from src.analysis.take_profit import TakeProfitCalculator
from src.analysis.volume_analyzer import VolumeAnalyzer

market = MarketData()

trend = TrendAnalyzer()
ema = EMAAnalyzer()
rsi = RSIAnalyzer()
macd = MACDAnalyzer()
sr = SupportResistanceAnalyzer()
candle = CandlestickAnalyzer()
generator = SignalGenerator()
atr = ATRAnalyzer()
tp = TakeProfitCalculator()
volume = VolumeAnalyzer()

for symbol in ["BTC-USD", "GC=F"]:

    data = market.get_data(symbol)

    result = generator.generate(data)
    levels = sr.detect(data)
    pattern = candle.detect(data)
    atr_data = atr.detect(data)
    volume_status = volume.detect(data)

    close = data["Close"]
    if hasattr(close, "columns"):
        close = close.iloc[:, 0]

    entry = float(close.iloc[-1])

    if result["signal"] == "BUY":
        trade = tp.calculate(entry, atr_data["buy_sl"])
    else:
        trade = tp.calculate(entry, atr_data["sell_sl"])

    print("=" * 60)
    print(symbol)
    print("=" * 60)
    print(f"Trend       : {result['trend']}")
    print(f"EMA         : {result['ema']}")
    print(f"RSI         : {result['rsi']}")
    print(f"MACD        : {result['macd']}")
    print(f"Pattern     : {pattern}")
    print(f"Volume      : {volume_status}")
    print(f"Support     : {levels['support']}")
    print(f"Resistance  : {levels['resistance']}")
    print(f"ATR         : {atr_data['atr']}")
    print(f"Entry       : {trade['entry']}")
    print(f"Stop Loss   : {trade['stop_loss']}")
    print(f"Take Profit : {trade['take_profit']}")
    print(f"R:R         : {trade['risk_reward']}")
    print("-" * 60)
    print(f"SIGNAL      : {result['signal']}")
    print(f"CONFIDENCE  : {result['confidence']}%")
    print()
