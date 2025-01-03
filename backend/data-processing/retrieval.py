import yfinance as yf 

def retrieval(symbols):
    data = {}
    for symbol in symbols:
        stock_data = yf.download(symbol, start="2010-01-01", end="2024-12-31")
        stock_data.to_csv(f"data/{symbol}_historical_data.csv")
        if not stock_data.empty:
            data[symbol] = stock_data
    return data

symbols = ["NVDA", "RGTI", "RIVN", "LCID", "TSLA", "AAPL", "F", "BA", "UBER", "FSLR", "GM", "MU", "PLTR", "WBA", "MRNA", "PFE", "EL", "ADBE", "GOOG", "AMZN", "MSFT"]
data = retrieval(symbols)