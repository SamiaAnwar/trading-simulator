from app.data_fetcher import get_live_data, get_features
from app.predictor import predict, trade_decision
from app.trade import portfolio, execute_trade, calculate_portfolio_value, portfolio_reset
# from data_fetcher import get_live_data, get_features
# from predictor import predict, trade_decision
# from trade import portfolio, execute_trade, calculate_portfolio_value

from datetime import date, timedelta 
import pandas as pd

#Input: symbols
#Output: trade_history, profit_history 
FEATURES = ['Close', 'EMA_5', 'MA_5', 'Lag_2', 'MA_10', 'Lag_1']

def trades(symbols):
    #portfolio_reset()
    # 1) Get features from [31, 60] trading days ago
    past_features = {} #Contains daily datapoints from the past ~30 trading days 
    dates = {}
    for symbol in symbols:
        sym_feats = []
        df, sym_date = get_live_data(symbol, date.today() - timedelta(113+42), date.today() - timedelta(57))
        df = df.tail(40) 
        sym_date = sym_date.tail(40).head(30)
        for i in range(30):
            feature_data = get_features(df[i:i+10], FEATURES)
            sym_feats.append(feature_data)
        past_features[symbol] = sym_feats
        dates[symbol] = sym_date
    
    # 2) Make Predictions, Decisions and record the trade  
    trade_history = []
    for symbol in symbols:
        daily_prediction = [] 
        for i, day in enumerate(past_features[symbol]):
            prediction = predict(day.T)
            action = trade_decision(prediction)
            executed = execute_trade(portfolio, symbol, action, 1, prediction['CURR_CLOSE'])
            
            if action != 'HOLD' and executed['status'] != 'failure':
                trade = {}
                trade['symbol'] = symbol
                trade['action'] = action
                trade['date'] = dates[symbol].iloc[i]
                trade['price'] = prediction['CURR_CLOSE']
                trade_history.append(trade)
            
    trade_history = sorted(trade_history, key=lambda d: d['date'])
    return trade_history

def portfolio_value(symbols): 
    curr_mo = {}
    dates = []
    for symbol in symbols:
        curr_mo[symbol], dates = get_live_data(symbol, date.today() - timedelta(56), date.today())
        curr_mo[symbol] = curr_mo[symbol].head(30)
        dates = dates.head(30)
    portfolio_values = [0]*30
    for i in range(len(dates)):
        portfolio_values[i] = (dates[i], calculate_portfolio_value(portfolio, curr_mo, i))
    
    return portfolio_values

def compare_predictions(symbol):
    #Get last month's closing prices
    curr_mo, dates = get_live_data(symbol, date.today() - timedelta(56), date.today())
    #Get month's closing prices from 2 months ago 
    past_mo, _ = get_live_data(symbol, date.today() - timedelta(113+42), date.today() - timedelta(57))
    past_mo = past_mo.tail(40)
    pred_curr = [0]*30
    for i in range(30):
        features = get_features(past_mo[i:i+10], FEATURES)
        prediction = predict(features.T)['PRED_CLOSE']
        pred_curr[i] = prediction 
    
    output = [(dates.iloc[i], curr_mo.iloc[i], pred_curr[i]) for i in range(30)]
    return output