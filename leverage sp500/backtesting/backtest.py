import backtrader as bt
class MyStrategy(bt.Strategy):
    params = (
        ('hold_period', 78),  # Set default hold period to a full day
    )

    def __init__(self):
        self.sandp500 = self.datas[0]  # This will be the S&P500 data
        self.etf_long = self.datas[1]  # This will be the Long ETF data
        self.etf_short = self.datas[2]  # This will be the Short ETF data

        # Create a list to hold portfolio values
        self.portfolio_values = []
        self.timestamps = []

        # Create counters for each ETF
        self.etf_long_buys = 0
        self.etf_short_buys = 0

    def next(self):
        # Open positions at market open if conditions are met
        if len(self) % self.params.hold_period == 0 and not self.position:
            if self.sandp500.open[0] >= self.sandp500.close[-1]:
                self.buy(self.etf_long, size=1)
                self.etf_long_buys += 1 # Increment the counter
            #else:
                #self.buy(self.etf_short, size=1)
                #self.etf_short_buys += 1 # Increment the counter

        # Close any open positions after hold_period bars
        elif self.position and len(self) % self.params.hold_period == self.params.hold_period - 1:
            self.close()

        # Append current portfolio value
        self.timestamps.append(self.datas[0].datetime.date(0))  # using the first data feed's datetime
        self.portfolio_values.append(self.broker.getvalue())


class PandasData(bt.feed.DataBase):
    params = (
        ('datetime', None),
        ('open', -1),
        ('high', -1),
        ('low', -1),
        ('close', -1),
        ('volume', -1),
        ('openinterest', None),
    )

def run_backtest(strategy, df1, df2, df3, hold_period):
    cerebro = bt.Cerebro()

    data1 = bt.feeds.PandasData(dataname=df1)
    data2 = bt.feeds.PandasData(dataname=df2)
    data3 = bt.feeds.PandasData(dataname=df3)

    cerebro.adddata(data1)
    cerebro.adddata(data2)
    cerebro.adddata(data3)

    cerebro.addstrategy(strategy, hold_period=hold_period)
    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')

    results = cerebro.run()

    return results


