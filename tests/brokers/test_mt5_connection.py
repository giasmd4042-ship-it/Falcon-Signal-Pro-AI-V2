from src.brokers.mt5_broker import mt5_broker


def test_mt5_connection():

    result = mt5_broker.connect()

    assert result is True

    print("MT5 Connection Test Passed")

    mt5_broker.disconnect()
