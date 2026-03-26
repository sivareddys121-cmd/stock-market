

import yfinance as yf

import pandas as pd


def get_stock_data(symbol):
    df = yf.download(symbol, period="1y")
    df.reset_index(inplace=True)
    return df

def preprocess_data(df):
    df['Daily Return'] = (df['Close'] - df['Open'])/df['Close']
    df['7 day MA'] = df['Close'].rolling(7).mean()
    df['30 day MA'] = df['Close'].rolling(30).mean()
    df['52 High'] = df['Close'].rolling(252).max()
    df['52 Low'] = df['Close'].rolling(252).min()
    df.fillna(0, inplace=True)
    return df