# TODAYS OBJECTIVE
# GET EVERYTHING SETUP (GIT AND ALSO PYCHARM, EVERYTHING RUNNING WELL)
# DATA RECOLLECTION ALSO DONE

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import statsmodels.api as sm


'''
# Given history, we are going to use vanguard funds
'VFICX' Vanguard Intermediate Term
'VWEHX' Vanguard High Yield Corporate Fund
'VFISX' Vanguard Short Term Treasury Fund
'SPY'
"^VIX"
"^IRX" TBill 3 month
'''

tickers_funds = ['VFICX', 'VWEHX', 'VFISX','SPY']
tickers_others = ['^VIX', '^IRX']
df = yf.download(tickers_funds + tickers_others, start = '2000-01-01', end = '2024-06-30')
df = df.resample('M').last()
df = df['Adj Close']
rets = np.log(df[tickers_funds] / df[tickers_funds].shift(1)).dropna()
rets['IRX'] = df['^IRX']/12/100
df_fin = rets.copy()
df_fin['VIX'] = df['^VIX']
df_fin['VIX_change'] = df_fin['VIX'] - df_fin['VIX'].shift(1)
df_fin = df_fin.dropna()

# 3. Compute cumulative returns
cum_logrets = rets.cumsum()
cum_rets = np.exp(cum_logrets) - 1
#cum_rets.plot()

# VIX orthogonal
x = sm.add_constant(df_fin['SPY'])
print(df_fin['VIX_change'], x)
model = sm.OLS(df_fin['VIX_change'],x).fit()
residuals = model.resid
df_fin['VIX_orthogonal'] = residuals

# Sharpe ratios
df_sharpe = rets.copy()
df_sharpe = df_sharpe.sub(rets['IRX'], axis = 0)
sharpe = df_sharpe.mean()/df_sharpe.std()
print(sharpe)


# Next steps

# GIT REPO SEND 20 MINUTES BREAK
# 4. Functions
# GIT REPO SEND 10 MINUTES BREAK
# 5. Am I going to include more information? YES. USE PSEUDO CODE AI
# GIT REPO SEND 20 MINUTES BREAK
# 6. Add a code to save graphs
# GIT REPO SEND 10 MINUTES BREAK
# IMPORTANTE: 9 PM CORTE, ENVIAR ESTO Y VERANO A MAIL

# MONDAY
# 1. Compute the yield spreads (BBG data?)


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
