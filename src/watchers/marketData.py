from database.sqlite import connectToSQLite
# from database.entities.MarketData import MarketData
# from sqlalchemy import create_engine, MetaData

def watchMarketData(symbol): 
    print('\nWatching data for ' + symbol)
    connectionAttributes = connectToSQLite()
    connection = connectionAttributes['engine'].connect()
    market_data = connectionAttributes['tables']['market_data']
    # metadata = MetaData(bind=engine)
    # market_data = MarketData(metadata)

    insert = market_data.insert()

    new_market_data = insert.values(
        symbol=symbol,
        currentPrice=0.135,
        value="0.135",
        percentage="%10",
        timestamp="2020-26-10"
    )

    connection.execute(new_market_data)

    # insert = tables



