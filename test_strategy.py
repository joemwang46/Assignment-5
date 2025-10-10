import pytest
from unittest.mock import MagicMock
from strategy import ThresholdStrategy

@pytest.fixture
def mock_broker():
    return MagicMock()

def test_buy_signal(mock_broker):
    strategy = ThresholdStrategy(mock_broker, threshold=100)
    strategy.run([101, 99])
    mock_broker.send_order.assert_called_once_with("BUY", qty=100)

def test_no_trade_on_empty(mock_broker):
    strategy = ThresholdStrategy(mock_broker)
    strategy.run([])
    mock_broker.send_order.assert_not_called()
