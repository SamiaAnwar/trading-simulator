import os
import pickle 
import json
import pandas as pd   
from io import StringIO

path = os.environ['HOME']
with open( path + '/Desktop/stock-market-predictor/backend/model/predictor_model.pkl', 'rb') as f:
    model = pickle.load(f)
FEATURES = ["Close", "EMA_5", "MA_5", "Lag_2", "MA_10", "Lag_1"]

def predict(daily_feature):
    if model is None:
        return {"status": "error", "message": "Model not loaded"}
    prediction = model.predict(daily_feature)
    return {'CURR_CLOSE': float(daily_feature['Close'].iloc[0]), 'PRED_CLOSE': prediction[0]}

def trade_decision(prediction, buy_threshold=0.05, sell_threshold=0.05, transaction_cost=0.005):
    curr_price = prediction['CURR_CLOSE']
    future_price = prediction['PRED_CLOSE']

    absolute_buy_threshold = (buy_threshold + transaction_cost)*curr_price
    absolute_sell_threshold = (sell_threshold + transaction_cost)*curr_price

    price_diff = future_price - curr_price

    if price_diff > absolute_buy_threshold:
        return 'BUY'
    elif (-1)*price_diff > absolute_sell_threshold:
        return 'SELL'
    else:
        return 'HOLD'

def trade_decision_allPred(predictions, buy_threshold=0.05, sell_threshold=0.05, transaction_cost=0.005):
    #Can potentially associate it with date (?) 
    decisions = []
    for prediction in predictions:
        curr_price = prediction['CURR_CLOSE']
        future_price = prediction['PRED_CLOSE']

        absolute_buy_threshold = (buy_threshold + transaction_cost)*curr_price
        absolute_sell_threshold = (sell_threshold + transaction_cost)*curr_price

        price_diff = future_price - curr_price

        if price_diff > absolute_buy_threshold:
            decisions.append('BUY')
        elif (-1)*price_diff > absolute_sell_threshold:
            decisions.append('SELL')
        else:
            decisions.append('HOLD')

    return decisions
    
#Outputs predicted future close price and current features 
def predict_all(inputs):
    if model is None:
        return {"status": "error", "message": "Model not loaded"}
    
    predictions = {}
    for symbol in inputs:
        data = inputs[symbol]
        df = pd.DataFrame(eval(data), index=[1])
        prediction = model.predict(df)
        #print("Today's Close:" + df['Close'].to_string(index=False) + " Next month prediction: " + str(prediction))
        predictions[symbol] = {'CURR_CLOSE': float(df['Close'].iloc[0]), 'PRED_CLOSE': prediction[0]}
    
    return predictions

def trade_decision_all(predictions, buy_threshold=0.05, sell_threshold=0.05, transaction_cost=0.005):

    decisions = {}

    for symbol in predictions:
        curr_price = predictions[symbol]['CURR_CLOSE']
        future_price = predictions[symbol]['PRED_CLOSE']

        absolute_buy_threshold = (buy_threshold + transaction_cost)*curr_price
        absolute_sell_threshold = (sell_threshold + transaction_cost)*curr_price

        price_diff = future_price - curr_price

        if price_diff > absolute_buy_threshold:
            decisions[symbol] = 'BUY'
        elif (-1)*price_diff > absolute_sell_threshold:
            decisions[symbol] = 'SELL'
        else:
            decisions[symbol] = 'HOLD'

    return decisions