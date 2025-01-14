from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from historical_data import fetch_historical_data, combineSymbols
from model_assessment import feature_importance, model_metrics
import pickle



SYMBOLS = ["NVDA", "RGTI", "RIVN", "LCID", "TSLA", "AAPL", "F", "BA", "UBER", "FSLR", "GM", "MU", "PLTR", "WBA", "MRNA", "PFE", "EL", "ADBE", "GOOG", "AMZN", "MSFT"]
FEATURES = ['MA_5', 'MA_10', 'Volume_Change', 'Close_Change', 'EMA_5', 'Lag_1', 'Lag_2']

def train(symbols, features):
    data = fetch_historical_data(symbols, features, '2025-01-07', '5d')
    data = combineSymbols(data)

    X = data[features]
    y = data['Close'].shift(-1).dropna()
    X = X[:-1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    selected_features = feature_importance(model, features)
    X_train_selected = X_train[selected_features]
    # Retrain the model
    model.fit(X_train_selected, y_train)

    X_test_selected = X_test[selected_features]
    model_metrics(model, X_test_selected, y_test)
    return model 

model = train(SYMBOLS, FEATURES)