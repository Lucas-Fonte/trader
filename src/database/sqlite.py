from sqlalchemy import create_engine, MetaData
from .entities.MarketData import MarketData
from .entities.MarketOrder import MarketOrder
from .entities.MarketStrategy import MarketStrategy


def connectToSQLite(): 
    connectionAttributes = {}

    engine = create_engine('sqlite:///./data/market_data.db', echo=True)
    metadata = MetaData(bind=engine)

    tables = {};

    tables['market_data'] = MarketData(metadata)
    tables['market_order'] = MarketOrder(metadata)
    tables['market_strategy'] = MarketStrategy(metadata)
    
    
    metadata.create_all()
    print('\nConnected to SQLite')

    connectionAttributes['engine'] = engine
    connectionAttributes['tables'] = tables

    return connectionAttributes