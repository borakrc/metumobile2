from AlacarteMenuBridge import AlacarteMenuBridge

class Alacarte:
    def __init__(self):
        pass
    
    def getUpcomingAlacarte(self, version):
        return AlacarteMenuBridge().getUpcomingAlacarteMenu(version if version >= 1.1 else 1.0)

