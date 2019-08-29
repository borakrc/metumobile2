from AlacarteBridge import AlacarteBridge

class Alacarte:
    def __init__(self):
        pass
    
    def getUpcomingAlacarte(self, version):
        return AlacarteBridge().getUpcomingAlacarteMenu(version if version >= 1.1 else 1.0)

