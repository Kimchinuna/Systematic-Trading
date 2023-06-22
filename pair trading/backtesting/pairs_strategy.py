import backtrader as bt

class PairsTradingStrategy(bt.Strategy):
    def __init__(self):
        self.data1 = self.datas[0]
        self.data2 = self.datas[1]

    def next(self):
        if self.data1 - self.data2 > 1.0:
            # Enter spread (buy stock1 and sell stock2)
            self.buy(data=self.data1)
            self.sell(data=self.data2)
        elif self.data1 - self.data2 < -1.0:
            # Exit spread (sell stock1 and buy stock2)
            self.sell(data=self.data1)
            self.buy(data=self.data2)
