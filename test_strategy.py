import pandas as pd

def test_signals_length(strategy, prices):
    sig = strategy.generate_signals(prices)
    assert len(sig) == len(prices)

def test_signals_values(strategy, prices):
    sig = strategy.generate_signals(prices)
    assert set(sig.unique()).issubset({-1, 0, 1})

def test_no_signals_on_flat_prices(strategy):
    prices = pd.Series([100] * 10)
    sig = strategy.generate_signals(prices)
    assert all(s == 0 for s in sig)