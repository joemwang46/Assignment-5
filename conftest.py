import numpy as np, pandas as pd, pytest
from strategy import VolatilityBreakoutStrategy
from broker import Broker

@pytest.fixture
def prices():
    # deterministic rising series
    return pd.Series(np.linspace(100, 120, 200))

@pytest.fixture
def strategy():
    return VolatilityBreakoutStrategy()

@pytest.fixture
def broker():
    return Broker(cash=1000000)