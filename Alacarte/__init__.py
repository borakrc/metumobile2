from MongoDatabase import MongoDatabase


class Alacarte:
    def __init__(self):
        pass

    def getUpcomingSchedule(self, version):
        return MongoDatabase().getUpcomingCafeteriaMenu(version if version >= 1.1 else 1.0)
