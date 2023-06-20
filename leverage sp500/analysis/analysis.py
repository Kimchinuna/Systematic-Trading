import numpy as np
import pandas as pd
import scipy as stats
import statsmodels.api as sm

def calculate_alpha_beta(returns, benchmark_returns):
    benchmark_returns = sm.add_constant(benchmark_returns)  # Add a constant to the benchmark returns
    model = sm.OLS(returns, benchmark_returns)
    results = model.fit()

    alpha = results.params[0]
    beta = results.params[1]

    return alpha, beta

def calculate_information_ratio(returns, benchmark_returns):
    """
    Calculate the information ratio of a strategy.

    Parameters
    ----------
    returns : pandas.Series
        The returns of the strategy.
    benchmark_returns : pandas.Series
        The returns of the benchmark.

    Returns
    -------
    information_ratio : float
        The information ratio of the strategy.
    """
    return_diff = returns - benchmark_returns
    information_ratio = np.mean(return_diff) / np.std(return_diff)

    return information_ratio
def calculate_annualized_return(daily_returns):
    """
    Calculate the annualized return of the strategy.
    """
    annualized_return = np.mean(daily_returns) * 252
    return annualized_return

def calculate_volatility(daily_returns):
    """
    Calculate the annualized volatility of the strategy.
    """
    volatility = np.std(daily_returns) * np.sqrt(252)
    return volatility

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.02):
    """
    Calculate the Sharpe ratio of the strategy.
    """
    annualized_return = calculate_annualized_return(daily_returns)
    volatility = calculate_volatility(daily_returns)
    sharpe_ratio = (annualized_return - risk_free_rate) / volatility
    return sharpe_ratio

def calculate_sortino_ratio(daily_returns, risk_free_rate=0.02):
    """
    Calculate the Sortino ratio of the strategy.
    """
    annualized_return = calculate_annualized_return(daily_returns)
    downside_returns = -daily_returns[daily_returns < 0]
    annualized_downside_volatility = np.std(downside_returns) * np.sqrt(252)
    sortino_ratio = (annualized_return - risk_free_rate) / annualized_downside_volatility
    return sortino_ratio

def calculate_max_drawdown(portfolio_values):
    """
    Calculate the maximum drawdown of the strategy.
    """
    cumulative_returns = (1 + pd.Series(portfolio_values)).cumprod()
    running_max = np.maximum.accumulate(cumulative_returns.dropna())
    drawdown = (cumulative_returns)/running_max - 1.0
    max_drawdown = drawdown.min()
    return max_drawdown

def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    """
    Calculate the Sharpe ratio based on the return series of a strategy.
    """
    return (returns.mean() - risk_free_rate) / returns.std()

def calculate_drawdown(return_series):
    """
    Calculates the largest peak-to-trough drawdown of the return series, as well as the duration of the drawdown.
    """
    # TODO: Calculate drawdown here
    pass

# Include any other metrics you want to analyze here
