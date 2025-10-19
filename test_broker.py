import pytest

def test_buy_and_sell_updates_cash_and_pos(broker):
    broker.market_order("buy", 2, 10.0)
    assert (broker.position, broker.cash) == (2, 1000000 - 20.0)

def test_rejects_bad_orders(broker):
    with pytest.raises(ValueError):
        broker.market_order("buy", 0, 10)

def test_sell_without_position_raises(broker):
    with pytest.raises(ValueError):
        broker.market_order("sell", 1, 10)

def test_partial_sell(broker):
    broker.market_order("buy", 5, 10.0)
    broker.market_order("sell", 2, 12.0)
    assert (broker.position, broker.cash) == (3, 1000000 - 50.0 + 24.0)

def test_full_sell(broker):
    broker.market_order("buy", 3, 15.0)
    broker.market_order("sell", 3, 20.0)
    assert (broker.position, broker.cash) == (0, 1000000 - 45.0 + 60.0)

def test_insufficient_cash_raises(broker):
    with pytest.raises(ValueError):
        broker.market_order("buy", 2000, 1000.0)

def test_insufficient_position_raises(broker):
    broker.market_order("buy", 5, 10.0)
    with pytest.raises(ValueError):
        broker.market_order("sell", 6, 12.0)
