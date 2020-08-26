from services.metaTrader import connectToMetaTrader
from watchers.marketData import watchMarketData

def getMarketData(symbol): 
    connectToMetaTrader()

    print('\nGetting data for ' + symbol)

    watchMarketData(symbol)
