from MysqlDatabase import MysqlDatabase

class Alacarte:
    def __init__(self):
        pass
    
    def getUpcomingAlacarte(self, version):
        return MysqlDatabase().getUpcomingAlacarteMenu(version if version >= 1.1 else 1.0)

