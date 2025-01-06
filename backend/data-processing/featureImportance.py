import matplotlib.pyplot as plt 
def featureImportance(feature_names, model):
    importances = model.feature_importances_
    feature_importance = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
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
