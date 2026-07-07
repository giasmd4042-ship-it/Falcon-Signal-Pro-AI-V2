from src.analysis.ai_score_engine import AIScoreEngine

engine = AIScoreEngine()

result = {
    "trend": "BULLISH",
    "ema": "BULLISH",
    "macd": "BEARISH",
    "rsi": "OVERSOLD (25.83)",
    "signal": "BUY"
}

score = engine.calculate(
    result=result,
    pattern="BULLISH ENGULFING",
    volume="HIGH VOLUME",
    breakout="NO BREAKOUT"
)

print("=" * 60)
print(score)
