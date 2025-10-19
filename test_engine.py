from unittest.mock import MagicMock
from engine import Backtester
import pytest

# example
def test_engine_uses_tminus1_signal(prices, broker, strategy, monkeypatch):
    # Force exactly one buy at t=10 by controlling signals
    fake_strategy = MagicMock()
    fake_strategy.generate_signals.return_value = prices*0
    fake_strategy.generate_signals.return_value.iloc[9] = 1  # triggers buy at t=10
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    cash = 1000000 - float(prices.iloc[10]) * 100
    assert broker.position == 100
    assert broker.cash == cash

def test_engine_no_trades_on_zero_signals(prices, broker, strategy):
    # Force all zero signals
    fake_strategy = MagicMock()
    fake_strategy.generate_signals.return_value = prices*0
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    assert broker.position == 0
    assert broker.cash == 1000000

def test_engine_sells_position(prices, broker, strategy):
    # Force buy at t=10 and sell at t=20
    fake_strategy = MagicMock()
    fake_strategy.generate_signals.return_value = prices*0
    fake_strategy.generate_signals.return_value.iloc[9] = 1   # buy at t=10
    fake_strategy.generate_signals.return_value.iloc[19] = -1  # sell at t=20
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    assert broker.position == 0
    expected_cash = 1000000 - float(prices.iloc[10])*100 + float(prices.iloc[20])*100
    assert broker.cash == expected_cash

def test_engine_handles_insufficient_cash(prices, broker, strategy):
    # Force multiple buys exceeding cash
    fake_strategy = MagicMock()
    fake_strategy.generate_signals.return_value = prices*0
    for i in range(0, 50, 5):
        fake_strategy.generate_signals.return_value.iloc[i] = 1  # buy signals
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    # Ensure position and cash are consistent with max buys possible
    max_affordable_buys = int(1000000 // float(prices.iloc[0]))
    assert broker.position <= max_affordable_buys
    assert broker.cash >= 0

def test_engine_handles_insufficient_position(prices, broker, strategy):
    # Force sells without enough position
    fake_strategy = MagicMock()
    fake_strategy.generate_signals.return_value = prices*0
    fake_strategy.generate_signals.return_value.iloc[5] = -1  # sell at t=6 without position
    with pytest.raises(ValueError):
        bt = Backtester(fake_strategy, broker)
        eq = bt.run(prices)

