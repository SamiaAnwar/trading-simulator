from retrieval import retrieval
from featureCreation import featureCreation
#Data Retrieval 
symbols = ["NVDA", "RGTI", "RIVN", "LCID", "TSLA", "AAPL", "F", "BA", "UBER", "FSLR", "GM", "MU", "PLTR", "WBA", "MRNA", "PFE", "EL", "ADBE", "GOOG", "AMZN", "MSFT"]
data = retrieval(symbols)
#Feature Creation 
features = featureCreation(data)