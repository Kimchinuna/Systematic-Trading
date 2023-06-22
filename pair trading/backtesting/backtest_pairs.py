import backtrader as bt

def backtest(data1, data2, strategy):
    # Create a cerebro entity
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(10000.0)  # sets the initial cash

    # Add data feeds to cerebro
    cerebro.adddata(data1)
    cerebro.adddata(data2)

    # Add a strategy
    cerebro.addstrategy(strategy)

    # Run the backtest
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    return cerebro

