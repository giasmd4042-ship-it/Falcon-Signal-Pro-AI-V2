from src.analysis.trade_logger import TradeLogger

logger = TradeLogger()

plan = {
    "symbol": "BTC-USD",
    "signal": "BUY",
    "entry": 63150.40,
    "stop_loss": 62598.78,
    "take_profit": 64253.64,
    "confidence": 75,
    "ai_score": 75,
    "grade": "A"
}

print(logger.log(plan))
