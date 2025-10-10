class ThresholdStrategy:
    def __init__(self, broker, threshold=100):
        self.broker = broker
        self.threshold = threshold

    def run(self, prices):
        if not prices:
            return  # no action on empty input
        if prices[-1] < self.threshold:
            self.broker.send_order("BUY", qty=100)
