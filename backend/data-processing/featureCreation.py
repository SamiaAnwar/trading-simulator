#The new features are derived from closing and volume values 
#New Features includes: 
def featureCreation(data, window=5):
    features = {}
    for symbol, df in data.items():
        df['MA_5'] = df['Close'].rolling(window=5).mean()
        df['MA_10'] = df['Close'].rolling(window=10).mean()
        df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
        df['Lag_1'] = df['Close'].shift(1)
        df['Lag_2'] = df['Close'].shift(2)
        df['Volume_Change'] = df['Volume'].pct_change()       
        df['Close_Change'] = df['Close'].pct_change()         
        features[symbol] = df[['MA_5', 'MA_10', 'Volume_Change', 'Close_Change', 'Close', 'EMA_5', 'Lag_1', 'Lag_2']]
    return features


