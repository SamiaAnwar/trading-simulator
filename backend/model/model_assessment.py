import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np 
import pandas as pd 

def feature_importance(model, features):

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

    return selected_features

def model_metrics(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae}")

    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    r2 = r2_score(y_test, y_pred)
    print(f"R-squared: {r2}")

def model_visualisation(model, symbols, X_test, y_test):
    y_pred = model.predict(X_test)

    
    plt.plot(y_test,label='actual')
    plt.plot(y_pred, label='predicted') 
    plt.xlabel('Time')
    plt.ylabel('Closing Price')
    plt.legend(loc="upper left")
    plt.title(f'Predicted Closing vs. Actual')
    plt.show()
