def targetExtraction(data, window=5):
    target = {}
    for symbol, df in data.items():
        target[symbol] = df['Close']
    return target