import os
import pickle 
import json
import pandas as pd   
from io import StringIO

from data_fetcher import get_live_data

path = os.environ['HOME']
with open( path + '/Desktop/stock-market-predictor/backend/model/predictor_model.pkl', 'rb') as f:
    model = pickle.load(f)
FEATURES = ["Close", "EMA_5", "MA_5", "Lag_2", "MA_10", "Lag_1"]

#Outputs predicted future close price and current features 
def predict(inputs):
    if model is None:
        return {"status": "error", "message": "Model not loaded"}
    
    for symbol in inputs:
        data = inputs[symbol]
        df = pd.DataFrame(eval(data), index=[1])
        prediction = model.predict(df)
        print("Today's Close:" + df['Close'].to_string(index=False) + " Next month prediction: " + str(prediction))

input = get_live_data(['AAPL', 'GOOG'])
predict(input)
