def featureImportance(feature_names, model):
    importances = model.feature_importances_
    feature_importance = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
    for feature, importance in feature_importance:
        print(f"{feature}: {importance:.4f}")
