from data_fetcher import get_live_data, get_features
from predictor import predict, trade_decision
from datetime import date, timedelta
import pandas as pd

#Input: symbols
#Output: trade_history, profit_history 
FEATURES = ['Close', 'EMA_5', 'MA_5', 'Lag_2', 'MA_10', 'Lag_1']

def backtest(symbols):
    # 1) Get features from [31, 60] trading days ago
    past_features = {} #Contains daily datapoints from the past ~30 trading days 
    for symbol in symbols:
        sym_feats = []
        df = get_live_data(symbol, date.today() - timedelta(113+42), date.today() - timedelta(57))
        df = df.tail(40) 
        for i in range(30):
            feature_data = get_features(df[i:i+10], FEATURES)
            sym_feats.append(feature_data)
        past_features[symbol] = sym_feats
    
    # 2) Make Predictions and Decisions 
    predictions = {} 
    decisions = {} 

    for symbol in symbols:
        daily_prediction = [] 
        for day in past_features[symbol]:
            #print(day.shape)
            prediction = predict(day.T)
            daily_prediction.append(prediction)
        predictions[symbol] = daily_prediction
        decisions[symbol] = trade_decision(daily_prediction)

    # 3) Get closing prices from [0, 30] days ago 
    curr_mo = {}
    for symbol in symbols:
        curr_mo[symbol] = get_live_data(symbol, date.today() - timedelta(56), date.today()).head(30)
    print(len(decisions['AAPL']))
    print(len(predictions['AAPL']))  
    print(len(curr_mo['AAPL']))  

    #Execute a trade using price from 3) and decision from 2) 
    return 

backtest(['AAPL', 'UBER'])