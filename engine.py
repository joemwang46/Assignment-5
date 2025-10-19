import pandas as pd

class Backtester:
    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run(self, prices: pd.Series):
        signals = self.strategy.generate_signals(prices)

        signals = signals.shift(1).fillna(0)

        for price, signal in zip(prices, signals):
            if signal == 1:
                qty = 100
                self.broker.market_order("buy", qty, price)
            elif signal == -1:
                qty = 100
                self.broker.market_order("sell", qty, price)
        