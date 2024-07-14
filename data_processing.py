# TODAYS OBJECTIVE
# GET EVERYTHING SETUP (GIT AND ALSO PYCHARM, EVERYTHING RUNNING WELL)
# DATA RECOLLECTION ALSO DONE

import pandas as pd
import numpy as np
import yfinance as yf

'''
# Given history, we are going to use vanguard funds
'VFICX' Vanguard Intermediate Term
'VWEHX' Vanguard High Yield Corporate Fund
'VFISX' Vanguard Short Term Treasury Fund
'SPY'
"^VIX"
"^IRX" TBill 3 month
'''

df = yf.download(['VFICX', 'VWEHX', 'VUSXX', 'SPY','^VIX', '^IRX'], start = '2000-01-01', end = '2024-06-30')
df = df['Adj Close']
print(df)

# Next steps
# 1. deannualize risk free
# 1. Compute the yield spreads
# 2. Compute returns
# 3. Compute cumulative returns
# 4. Compute volatilities
# 5. Compute sharpe ratios
# 6. Generate VIX orthogonal?
# Do a check if we have table information
# 7. Am I going to include more information?
# AT 6 PM GIT REPO SEND

'''
data_grid, err = ek.get_data(['AAPL.O', 'IBM', 'GOOG.O', 'AMZN.O'],
                             ['TR.TotalReturnYTD', 'TR.WACCBeta',
                              'YRHIGH', 'YRLOW',
                              'TR.Ebitda', 'TR.GrossProfit'])
rets = np.log(raw[symbols] / raw[symbols].shift(1)).dropna()
(raw[symbols[:]] / raw[symbols[:]].iloc[0]).plot(figsize=(10, 6));
def add_lags(data, ric, lags):
    cols = []
    df = pd.DataFrame(data[ric])
    for lag in range(1, lags + 1):
        col = 'lag_{}'.format(lag)
        df[col] = df[ric].shift(lag)
        cols.append(col)
    df.dropna(inplace=True)
    return df, cols
dfs = {}
for sym in data.columns:
    df, cols = add_lags(data, sym, lags)
    dfs[sym] = df
split = int(len(dfs[sym]) * 0.8)
 train = df.iloc[:split]
 test = df.iloc[split:]
 def add_lags(data, ric, lags, window=50):
    cols = []
    df = pd.DataFrame(data[ric])
    df.dropna(inplace=True)
    df['r'] = np.log(df / df.shift())
    df['sma'] = df[ric].rolling(window).mean()
    df['min'] = df[ric].rolling(window).min()
    df['max'] = df[ric].rolling(window).max()
    df['mom'] = df['r'].rolling(window).mean()
    df['vol'] = df['r'].rolling(window).std()
    df.dropna(inplace=True)
    df['d'] = np.where(df['r'] > 0, 1, 0)
    features = [ric, 'r', 'd', 'sma', 'min', 'max', 'mom', 'vol']
    for f in features:
        for lag in range(1, lags + 1):
            col = f'{f}_lag_{lag}'
            df[col] = df[f].shift(lag)
            cols.append(col)
    df.dropna(inplace=True)
    return df, cols
# remember to normalize data
def add_lags(data, symbol, lags, window=20):
    cols = []
    df = data.copy()
    df.dropna(inplace=True)
    df['r'] = np.log(df / df.shift())
    df['sma'] = df[symbol].rolling(window).mean()
    df['min'] = df[symbol].rolling(window).min()
    df['max'] = df[symbol].rolling(window).max()
    df['mom'] = df['r'].rolling(window).mean()
    df['vol'] = df['r'].rolling(window).std()
    df.dropna(inplace=True)
    df['d'] = np.where(df['r'] > 0, 1, 0)
    features = [symbol, 'r', 'd', 'sma', 'min', 'max', 'mom', 'vol']
    for f in features:
        for lag in range(1, lags + 1):
            col = f'{f}_lag_{lag}'
            df[col] = df[f].shift(lag)
            cols.append(col)
    df.dropna(inplace=True)
    return df, cols
'''
