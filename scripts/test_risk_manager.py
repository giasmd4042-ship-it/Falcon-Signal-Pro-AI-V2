from src.analysis.risk_manager import RiskManager

rm = RiskManager()

result = rm.calculate(
    balance=10000,
    risk_percent=1,
    entry=63123.26,
    stop_loss=62567.34
)

print("=" * 60)
print(result)
