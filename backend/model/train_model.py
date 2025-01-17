from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


from model.historical_data import fetch_historical_data, combineSymbols
from model.model_assessment import feature_importance, model_metrics, model_visualisation
from datetime import date, timedelta
def train(symbols, features):
    #Fetching Data from Past Week 
    data = fetch_historical_data(symbols, features, date.today() - timedelta(7), '5d')
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

    model_visualisation(model, symbols, X_test_selected, y_test)
    return model 