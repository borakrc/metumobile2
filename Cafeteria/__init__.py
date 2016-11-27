class Cafeteria:
    def __init__(self):
        pass

    def getSchedule(self, version=1.0):
        from MongoDatabase import MongoDatabase
        return MongoDatabase().getCafeteriaMenu(version)

