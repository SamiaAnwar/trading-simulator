from retrieval import retrieval
from featureCreation import featureCreation
from targetExtraction import targetExtraction
from combineSymbols import combineSymbols
from randomForestModel import randomForestModel
from featureImportance import featureImportance
from modelAssessment import assess
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd 
#Data Retrieval 
symbols = ["NVDA", "RGTI", "RIVN", "LCID", "TSLA", "AAPL", "F", "BA", "UBER", "FSLR", "GM", "MU", "PLTR", "WBA", "MRNA", "PFE", "EL", "ADBE", "GOOG", "AMZN", "MSFT"]
one = ['NVDA']
data = retrieval(symbols)
#Feature Creation 
features = featureCreation(data)
training = combineSymbols(features)
#Test and Training Set Creation 
feature_names = ['MA_5', 'MA_10', 'Volume_Change', 'Close_Change', 'EMA_5', 'Lag_1', 'Lag_2']
X = training[feature_names]
y = training['Close']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Getting Random Forest Model 
rfmodel = randomForestModel(X_train, y_train)
#Visualise Feature Importance
featureImportance(feature_names, rfmodel)
#Assess the Model 
mae, mse, r2 = assess(rfmodel, X_test, y_test)
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-Squared: {r2}")
with open('models/stock_predictor.pkl', 'wb') as f:
    pickle.dump(rfmodel, f)


