import pandas as pd
def combineSymbols(features):
    combined = None
    for s, df in features.items():
        if combined is None :
            combined = df
        else:
            combined = pd.merge(combined, df, on='Date', how='outer', suffixes=('', f'_{s}'))
    return combined