from cronjob.index import Cronjob
from database.index import Database

class Main: 
    @staticmethod
    def start():
        print('Booting trader...')
        Database.start()
        Cronjob.start()
        

Main.start()

