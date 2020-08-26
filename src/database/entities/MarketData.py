from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float

def MarketData(metadata):
    return Table('market_data', metadata,
            Column('id', Integer, primary_key=True),
            Column('symbol', String(255)),
            Column('currentPrice', Float),
            Column('value', String(255)),
            Column('percentage', String(255)),
            Column('timestamp', String(255)))