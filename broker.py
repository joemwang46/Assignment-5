class Broker:
    def __init__(self, cash: float = 1_000_000):
        self.cash = cash
        self.position = 0

    def market_order(self, side: str, qty: int, price: float):
        cost = qty * price

        if qty <= 0:
            raise ValueError("Quantity must be positive.")
        if side == "buy":
            if self.cash >= cost:
                self.position += qty
                self.cash -= cost
            else:
                raise ValueError("Insufficient cash for buy order.")
        elif side == "sell":
            if self.position >= qty:
                self.position -= qty
                self.cash += cost
            else:
                raise ValueError("Insufficient position for sell order.")
        else:
            raise ValueError("Side must be 'buy' or 'sell'.")