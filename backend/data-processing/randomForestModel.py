from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
def randomForestModel(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model 