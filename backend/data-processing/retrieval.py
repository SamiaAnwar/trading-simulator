import yfinance as yf 

def retrieval(symbols):
    data = {}
    for symbol in symbols:
        stock_data = yf.download(symbol, start="2021-11-11", end="2024-12-31")
        #stock_data.to_csv(f"data/{symbol}_historical_data.csv")
        if not stock_data.empty:
            stock_data['Symbol'] = symbol
            data[symbol] = stock_data
    return data

