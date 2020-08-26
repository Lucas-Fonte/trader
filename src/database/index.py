from .sqlite import connectToSQLite

class Database: 
    @staticmethod
    def start():
        print('\nStarting database...')
        print('Database on')

        connectToSQLite()
