from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float

def MarketOrder(metadata):
    return Table('market_order', metadata,
            Column('id', Integer, primary_key=True),
            Column('action', String(255)),
            Column('positiveGain', Float),
            Column('negativeGain', Float),
            Column('positiveLoss', Float),
            Column('negativeLoss', Float),
            Column('symbol', String(255)),
            Column('currentPrice', Float),
            Column('value', String(255)),
            Column('percentage', String(255)),
            Column('timestamp', String(255)))