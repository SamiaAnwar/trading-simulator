from train_model import train
import pickle

SYMBOLS = ["NVDA", "RGTI", "RIVN", "LCID", "TSLA", "AAPL", "F", "BA", "UBER", "FSLR", "GM", "MU", "PLTR", "WBA", "MRNA", "PFE", "EL", "ADBE", "GOOG", "AMZN", "MSFT"]
FEATURES = ['MA_5', 'MA_10', 'Volume_Change', 'Close_Change', 'EMA_5', 'Lag_1', 'Lag_2']

def create_model():
    model = train(SYMBOLS, FEATURES)
    with open('predictor_model.pkl', 'wb') as f:
        pickle.dump(model, f)