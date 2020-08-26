from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float

def MarketStrategy(metadata):
    return Table('market_strategy', metadata,
            Column('id', Integer, primary_key=True),
            Column('strategy', String(255)),
            Column('positiveFactor', Float),
            Column('negativeFactor', Float))
