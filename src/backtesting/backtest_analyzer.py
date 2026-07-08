from datetime import datetime


class BacktestAnalyzer:
    """
    Falcon Signal Pro AI V3.29.0
    Backtest Intelligence Analyzer
    """

    def __init__(self):
        self.version = "V3.29.0"

    def analyze(self, results):

        if not results:
            return {
                "score": 0,
                "rating": "NO_DATA",
                "engine": self.version
            }

        total_profit = results.get(
            "total_profit",
            results.get("net_profit", 0)
        )

        win_rate = results.get(
            "win_rate",
            results.get("average_win_rate", 0)
        )

        trades = results.get(
            "trades",
            results.get("strategies", 0)
        )


        profit_score = min(
            max(total_profit / 10, 0),
            40
        )

        win_score = min(
            win_rate * 0.5,
            40
        )

        activity_score = min(
            trades * 2,
            20
        )


        intelligence_score = round(
            profit_score
            + win_score
            + activity_score,
            2
        )


        if intelligence_score >= 85:
            rating = "EXCELLENT"

        elif intelligence_score >= 70:
            rating = "GOOD"

        elif intelligence_score >= 50:
            rating = "AVERAGE"

        else:
            rating = "WEAK"


        return {
            "intelligence_score": intelligence_score,
            "rating": rating,
            "profit_score": round(profit_score,2),
            "win_score": round(win_score,2),
            "activity_score": round(activity_score,2),
            "timestamp": datetime.now().isoformat(),
            "engine": self.version
        }


backtest_analyzer = BacktestAnalyzer()
