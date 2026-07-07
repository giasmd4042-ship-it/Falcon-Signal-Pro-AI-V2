from src.analysis.trade_planner import TradePlanner

planner = TradePlanner()

result = {
    "signal": "BUY",
    "trend": "BULLISH",
    "confidence": 75
}

tp_data = {
    "entry": 63150.40,
    "stop_loss": 62598.78,
    "take_profit": 64253.64,
    "risk_reward": "1:2.0"
}

ai_score = {
    "percent": 75,
    "grade": "A"
}

plan = planner.create(
    "BTC-USD",
    result,
    tp_data,
    ai_score
)

print("=" * 60)
for k, v in plan.items():
    print(f"{k:15}: {v}")
