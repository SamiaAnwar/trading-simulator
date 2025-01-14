import yfinance as yf 
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import pandas as pd
import pickle

def fetch_data_tickers(tickers, features, start_date, duration):
    data = yf.download(list(tickers), start=start_date, period=duration, interval='1m')
    print(data.head)
    for feature in features:
        match feature:
            case 'MA_5':
                data['MA_5'] = data['Close'].rolling(window=5).mean()
            case 'MA_10':
                data['MA_10'] = data['Close'].rolling(window=10).mean()
            case 'EMA_5':
                data['EMA_5'] = data['Close'].ewm(span=5, adjust=False).mean()
            case 'Lag_1':
                data['Lag_1'] = data['Close'].shift(1)
            case 'Lag_2':
                data['Lag_2'] = data['Close'].shift(2)
            case 'Volume_Change':
                data['Volume_Change'] = data['Volume'].pct_change()
            case 'Close_Change':       
                data['Close_Change'] = data['Close'].pct_change() 
    data.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
    data.dropna(inplace=True)

    scaler = StandardScaler()
    data[features] = scaler.fit_transform(data[features])

    return data 
def fetch_historical_data(symbols, features, start_date, duration):
    historical_data = {}
    for symbol in symbols:
        df = yf.download(symbol, start=start_date, period=duration, interval='1m')
        df.reset_index(inplace=True)
        for feature in features:
            match feature:
                case 'MA_5':
                    df['MA_5'] = df['Close'].rolling(window=5).mean()
                case 'MA_10':
                    df['MA_10'] = df['Close'].rolling(window=10).mean()
                case 'EMA_5':
                    df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
                case 'Lag_1':
                    df['Lag_1'] = df['Close'].shift(1)
                case 'Lag_2':
                    df['Lag_2'] = df['Close'].shift(2)
                case 'Volume_Change':
                    df['Volume_Change'] = df['Volume'].pct_change()
                case 'Close_Change':       
                    df['Close_Change'] = df['Close'].pct_change() 
        df.replace([float('inf'), float('-inf')], float('nan'), inplace=True)
        df.dropna(inplace=True)

        scaler = StandardScaler()
        df[features] = scaler.fit_transform(df[features])

        historical_data[symbol] = df
    
    return historical_data
      
def combineSymbols(features):
    combined = None
    for s, df in features.items():
        if combined is None :
            combined = df
        else:
            combined = pd.merge(combined, df, on='Datetime', suffixes=('', f'_{s}'))

            #combined = pd.merge(combined, df, on='Datetime', how='outer', suffixes=('', f'_{s}'))
    return combined



symbols = ["NVDA", "RGTI", "RIVN", "LCID", "TSLA", "AAPL", "F", "BA", "UBER", "FSLR", "GM", "MU", "PLTR", "WBA", "MRNA", "PFE", "EL", "ADBE", "GOOG", "AMZN", "MSFT"]
features = ['MA_5', 'MA_10', 'Volume_Change', 'Close_Change', 'EMA_5', 'Lag_1', 'Lag_2']
data = fetch_historical_data(symbols, features, '2025-01-07', '5d')
#print(data.shape)
data = combineSymbols(data)
#data = fetch_data_tickers(symbols, features, '2025-01-07', '5d')
X = data[features]
y = data['Close'].shift(-1).dropna()
X = X[:-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

importances = model.feature_importances_

# Combine feature names with their importance scores
feature_importance = sorted(zip(features, importances), key=lambda x: x[1], reverse=True)

# Display the sorted feature importance
for feature, importance in feature_importance:
    print(f"{feature}: {importance:.4f}")

feature_names, importance_scores = zip(*feature_importance)

# Plot
plt.figure(figsize=(10, 6))
plt.barh(feature_names, importance_scores, color='skyblue')
plt.xlabel('Feature Importance')
plt.title('Feature Importance in Random Forest Model')
plt.gca().invert_yaxis()  # Invert to show the most important feature at the top
plt.show()

threshold = 0.05
selected_features = [feature for feature, importance in feature_importance if importance > threshold]
print(f"Selected Features: {selected_features}")

X_train_selected = X_train[selected_features]
X_test_selected = X_test[selected_features]

# Retrain the model
model.fit(X_train_selected, y_train)

y_pred = model.predict(X_test[selected_features])
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")
