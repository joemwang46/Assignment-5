from abc import ABC, abstractmethod
import pandas as pd

class Strategy(ABC):
    @abstractmethod
    def generate_signals(self, prices: pd.Series) -> pd.Series:
        pass

class VolatilityBreakoutStrategy(Strategy):
    def __init__(self, lookback=5, multiplier=2):
        self.lookback = int(lookback)
        self.multiplier = multiplier
        self.signals = None

    def generate_signals(self, prices):
        prices = pd.Series(prices).dropna()
        signals = pd.Series(0, index=prices.index, dtype=int)

        for idx in range(len(prices)):
            if idx < self.lookback:
                signals.iloc[idx] = 0
                continue

            recent = prices.iloc[idx - self.lookback: idx]
            mean = recent.mean()
            std = recent.std(ddof=1)
            upper = mean + self.multiplier * std
            lower = mean - self.multiplier * std
            current = prices.iloc[idx]

            if current > upper:
                signals.iloc[idx] = 1
            elif current < lower:
                signals.iloc[idx] = -1
            else:
                signals.iloc[idx] = 0

        return signals
            