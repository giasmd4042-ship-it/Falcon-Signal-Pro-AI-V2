"""
Falcon Signal Pro AI V2.0
Final Trade Planner
"""

class TradePlanner:

    def create(self, symbol, result, tp_data, ai_score):

        return {
            "symbol": symbol,
            "signal": result["signal"],
            "trend": result["trend"],
            "entry": tp_data["entry"],
            "stop_loss": tp_data["stop_loss"],
            "take_profit": tp_data["take_profit"],
            "risk_reward": tp_data["risk_reward"],
            "confidence": result["confidence"],
            "ai_score": ai_score["percent"],
            "grade": ai_score["grade"]
        }
