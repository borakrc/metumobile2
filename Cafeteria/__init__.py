class Cafeteria:
    def __init__(self):
        pass

    def getUpcomingSchedule(self, version):
        from MongoDatabase import MongoDatabase
        return MongoDatabase().getUpcomingCafeteriaMenu(version if version >= 1.1 else 1.0)

    def getAllMeals(self):
        from MongoDatabase import MongoDatabase
        return MongoDatabase().getAllCafeteriaMenu()



