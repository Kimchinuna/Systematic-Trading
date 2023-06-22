# Statistical Arbitrage Trading Strategy

This project is an implementation of a basic statistical arbitrage strategy known as pairs trading. The project involves the following steps:

1. Fetching data for the most active stocks on NASDAQ.
2. Identifying pairs of stocks that are cointegrated.
3. Implementing a pairs trading strategy on the identified pairs.
4. Backtesting the strategy using historical data.
5. Visualizing and analyzing the results of the backtest.

## Getting Started

### Prerequisites

To run the scripts in this project, you'll need to install the following Python libraries if you haven't already:

- pandas
- numpy
- statsmodels
- yfinance
- backtrader
- seaborn

You can install these libraries using pip:

```bash
pip install pandas numpy statsmodels yfinance backtrader seaborn
