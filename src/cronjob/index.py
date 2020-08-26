from .marketData import getMarketData

SYMBOL = 'WINV20'

class Cronjob: 
    @staticmethod
    def start():
        print('\nStarting Cronjob...')
        print('Cronjob running')

        getMarketData(SYMBOL)
