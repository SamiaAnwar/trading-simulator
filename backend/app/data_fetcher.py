import requests
import os 
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
def get_live_data(symbols):
    url = 'https://www.alphavantage.co/query'
    
    data = {}
    for symbol in symbols:
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '1min',
            'apikey': API_KEY
        }
        response = requests.get(url, params=params)
        symbol_data = response.json()

        if 'Time Series (1min)' in symbol_data:
            latest_time = list(symbol_data['Time Series (1min)'].keys())[0]
            latest_data = symbol_data['Time Series (1min)'][latest_time]
            data[symbol] = {
                'close': float(latest_data['4. close']),
                'volume':int(latest_data['5. volume'])
            }
    return data
