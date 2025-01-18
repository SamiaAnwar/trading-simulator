from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from model.historical_data import fetch_historical_data, combineSymbols
from model.model_assessment import feature_importance, model_metrics, model_visualisation
from datetime import date, timedelta

def train(symbols, features):
    #Fetching Data from Past Week 
    data = fetch_historical_data(symbols, features, date.today() - timedelta(365*2), date.today() - timedelta(1))
    data = combineSymbols(data)

    X = data[features]
    y = data['Close'].shift(-1).dropna()
    X = X[:-1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   
    rfmodel = RandomForestRegressor(n_estimators=100, random_state=42)
    rfmodel.fit(X_train, y_train)

    nnmodel = MLPRegressor(random_state=1, max_iter=500)
    nnmodel.fit(X_train, y_train)

    lrmodel = LinearRegression()
    lrmodel.fit(X_train, y_train)

    selected_features = feature_importance(rfmodel, features)
    X_train_selected = X_train[selected_features]

    # Retrain the model
    rfmodel.fit(X_train_selected, y_train)
    nnmodel.fit(X_train_selected, y_train)
    lrmodel.fit(X_train_selected, y_train)
    X_test_selected = X_test[selected_features]

    model_metrics(rfmodel, X_test_selected, y_test)

    model_visualisation(rfmodel, symbols, X[selected_features].iloc[:50,:], y.iloc[:50,:])

    return rfmodel, selected_features