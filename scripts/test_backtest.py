from src.analysis.market_data import MarketData
from src.analysis.backtest_engine import BacktestEngine

market = MarketData()
engine = BacktestEngine()

btc = market.get_data("BTC-USD")

result = engine.run(btc)

print("=" * 60)
print(result)
