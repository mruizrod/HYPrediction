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

def getYFdata(tickers, startd ='2000-01-01', endd = '2024-06-30'):
    df = yf.download(tickers, start = startd, end = endd)
    df = df.resample('M').last()
    df = df['Adj Close']
    return df

def getReturns(df,tickers_funds):
    rets = np.log(df[tickers_funds] / df[tickers_funds].shift(1)).dropna()
    rets['IRX'] = df['^IRX']/12/100
    cum_logrets = rets.cumsum()
    cum_rets = np.exp(cum_logrets) - 1
    # cum_rets.plot()
    return rets, cum_rets

def addVIXdata(df, orthogonal = True):
    df = df.rename(columns = {'^VIX': 'VIX'})
    df['VIX_change'] = df['VIX'] - df['VIX'].shift(1)
    df = df.dropna()
    if orthogonal:
        x = sm.add_constant(df['SPY'])
        model = sm.OLS(df['VIX_change'], x).fit()
        residuals = model.resid
        df['VIX_orthogonal'] = residuals
    return df

def getSharpeRatios(df):
    df_sharpe = df.copy()
    df_sharpe = df_sharpe.sub(rets['IRX'], axis=0)
    sharpe = df_sharpe.mean() / df_sharpe.std()
    return sharpe

def buildFeatures(data, ric, lags, window=12):
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

# Next steps
# Am I going to include more information? YES. USE PSEUDO CODE AI
# GIT REPO SEND 20 MINUTES BREAK
# 6. Add a code to save graphs
# GIT REPO SEND 10 MINUTES BREAK
# IMPORTANTE: 9 PM CORTE, ENVIAR ESTO Y VERANO A MAIL

# 1. Compute the yield spreads (BBG data?)


'''
data_grid, err = ek.get_data(['AAPL.O', 'IBM', 'GOOG.O', 'AMZN.O'],
                             ['TR.TotalReturnYTD', 'TR.WACCBeta',
                              'YRHIGH', 'YRLOW',
                              'TR.Ebitda', 'TR.GrossProfit'])
dfs = {}
for sym in data.columns:
    df, cols = add_lags(data, sym, lags)
    dfs[sym] = df
split = int(len(dfs[sym]) * 0.8)
 train = df.iloc[:split]
 test = df.iloc[split:]
# remember to normalize data
'''

if __name__ == '__main__':
    tickers_funds = ['VFICX', 'VWEHX', 'VFISX','SPY']
    tickers_others = ['^VIX', '^IRX']
    data = getYFdata(tickers_funds + tickers_others)
    data_new, cols = buildFeatures(data, 'VWEHX',lags = 6)