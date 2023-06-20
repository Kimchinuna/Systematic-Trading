# visualization/visualize.py
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('Set2')  # Set color palette
sns.set_style("darkgrid")

def plot_equity_curve(portfolio_values):
    plt.figure(figsize=(12, 6))  # Change the figure size here
    plt.plot(portfolio_values, color='blue')  # Change the line color here
    plt.title('Equity Curve')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.grid(True)
    plt.show()

def plot_drawdowns(drawdowns):
    """
    Plot drawdowns over time using Seaborn.
    """
    sns.lineplot(x=drawdowns.index, y=drawdowns)
    plt.title('Drawdown Over Time')
    plt.xlabel('Time')
    plt.ylabel('Drawdown')
    plt.show()

# Include any other plots or visualizations here
