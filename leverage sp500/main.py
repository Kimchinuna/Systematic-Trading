from data.data import fetch_data, preprocess_data
from backtesting.backtest import MyStrategy, run_backtest
from analysis.analysis import calculate_sharpe_ratio, calculate_drawdown
from visualization.visualize import plot_equity_curve, plot_drawdowns

# Fetch and preprocess data
sandp500_data = fetch_data('ES=F', '2015-01-01', '2020-12-31')
etf_data = fetch_data('SPXL', '2015-01-01', '2020-12-31')  # Replace with your ETF ticker

sandp500_data = preprocess_data(sandp500_data)
etf_data = preprocess_data(etf_data)

# Run backtest
results = run_backtest(MyStrategy, [sandp500_data, etf_data])

# Analyze results
sharpe_ratio = calculate_sharpe_ratio(results)
drawdown = calculate_drawdown(results)

# Visualize results
plot_equity_curve(results)
plot_drawdowns(drawdown)

# TODO: Add more detailed analysis and visualization as needed

#%%
