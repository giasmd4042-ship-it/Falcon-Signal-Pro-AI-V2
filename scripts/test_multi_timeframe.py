from src.analysis.multi_timeframe import MultiTimeframeAnalyzer

mtf = MultiTimeframeAnalyzer()

for symbol in ["BTC-USD", "GC=F"]:

    result = mtf.analyze(symbol)

    print("=" * 60)
    print(symbol)
    print("=" * 60)
    print("15m :", result["15m"])
    print("1H  :", result["1h"])
    print("4H  :", result["4h"])
    print("1D  :", result["1d"])
    print("-" * 60)
    print("OVERALL :", result["overall"])
    print("SCORE   :", result.get("score", "N/A"))
    print()

