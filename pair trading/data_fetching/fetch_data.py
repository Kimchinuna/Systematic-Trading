import yfinance as yf
from bs4 import BeautifulSoup
import requests

def get_most_active_stocks(exchange, count):
    # Define the URL of the webpage
    url = f"https://www.nasdaq.com/market-activity/{exchange}/most-active"
    # Send a GET request to the webpage
    response = requests.get(url)
    # Parse the webpage's contents
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the table with the most active stocks
    table = soup.find_all("table")[0]
    # Find all table rows
    rows = table.find_all("tr")
    # Extract the ticker symbols
    tickers = [row.find_all("td")[0].text for row in rows[1:]]
    # Return the specified number of ticker symbols
    return tickers[:count]


def fetch_data(symbols, start_date, end_date):
    return {symbol: yf.download(symbol, start=start_date, end=end_date) for symbol in symbols}
