from statsmodels.tsa.stattools import coint

def find_cointegrated_pairs(data):
    symbols = list(data.keys())
    cointegrated_pairs = []
    for i in range(len(symbols)):
        for j in range(i+1, len(symbols)):
            symbol1 = symbols[i]
            symbol2 = symbols[j]
            _, pvalue, _ = coint(data[symbol1]['Close'], data[symbol2]['Close'])
            if pvalue < 0.05:
                cointegrated_pairs.append((symbol1, symbol2))
    return cointegrated_pairs

#%%
