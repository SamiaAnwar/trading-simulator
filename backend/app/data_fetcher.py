import yfinance as yf 
import pandas as pd
from datetime import date, timedelta


#FEATURES = ['MA_5', 'MA_10', 'Volume_Change', 'Close_Change', 'EMA_5', 'Lag_1', 'Lag_2', 'Close', 'Volume']
FEATURES = ['Close', 'EMA_5', 'MA_5', 'Lag_2', 'MA_10', 'Lag_1']

def get_features(data, features):
    df = {}
    df['Close'] = data
    df = pd.DataFrame(df)
    for feature in features:
        match feature:
            case 'MA_5':
                df['MA_5'] = df['Close'].rolling(window=5).mean()
            case 'MA_10':
                df['MA_10'] = df['Close'].rolling(window=10).mean()
            case 'EMA_5':
                df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
            case 'Lag_1':
                df['Lag_1'] = df['Close'].shift(1)
            case 'Lag_2':
                df['Lag_2'] = df['Close'].shift(2)
            case 'Volume_Change':
                df['Volume_Change'] = df['Volume'].pct_change()
            case 'Close_Change':       
                df['Close_Change'] = df['Close'].pct_change() 
            case 'Datetime':
                df['Datetime'] = df['Datetime'].astype(str)
    df.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    return pd.DataFrame(df[features].iloc[-1])

def get_live_data(symbol, start, end):
    df = yf.Ticker(symbol).history(start=start, end=end, interval='1d')
    df.reset_index(inplace=True)
    return df['Close'], df['Date']

def get_live_data_features(symbols):
    data = {}
    for symbol in symbols:

        #Fetching Live Data 
        #df = yf.Ticker(symbol).history(start=date.today() - timedelta(85), end=date.today() - timedelta(64), interval='1d')
        df = yf.Ticker(symbol).history(start=date.today() - timedelta(22), end=date.today() - timedelta(1), interval='1d')
        df.reset_index(inplace=True)
        
        #Extracting relevant Feature Data 
        for feature in FEATURES:
            match feature:
                case 'MA_5':
                    df['MA_5'] = df['Close'].rolling(window=5).mean()
                case 'MA_10':
                    df['MA_10'] = df['Close'].rolling(window=10).mean()
                case 'EMA_5':
                    df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
                case 'Lag_1':
                    df['Lag_1'] = df['Close'].shift(1)
                case 'Lag_2':
                    df['Lag_2'] = df['Close'].shift(2)
                case 'Volume_Change':
                    df['Volume_Change'] = df['Volume'].pct_change()
                case 'Close_Change':       
                    df['Close_Change'] = df['Close'].pct_change() 
                case 'Datetime':
                    df['Datetime'] = df['Datetime'].astype(str)
        df.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
        df.dropna(inplace=True)

        #Getting the latest 
        data[symbol] = df[FEATURES].iloc[-1].to_json()

    return data