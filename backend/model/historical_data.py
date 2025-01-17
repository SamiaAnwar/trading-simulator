import yfinance as yf 
from sklearn.preprocessing import StandardScaler
import pandas as pd

def fetch_historical_data(symbols, features, start_date, duration):
    historical_data = {}
    for symbol in symbols:
        df = yf.download(symbol, start=start_date, period=duration, interval='1m')
        df.reset_index(inplace=True)
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

        #scaler = StandardScaler()
        #df[features] = scaler.fit_transform(df[features])

        historical_data[symbol] = df
    
    return historical_data

def combineSymbols(features):
    combined = None
    for s, df in features.items():
        if combined is None :
            combined = df
        else:
            combined = pd.merge(combined, df, on='Datetime', suffixes=('', f'_{s}'))

            #combined = pd.merge(combined, df, on='Datetime', how='outer', suffixes=('', f'_{s}'))
    return combined