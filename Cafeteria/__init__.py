class Cafeteria:
    def __init__(self):
        pass

    @staticmethod
    def getSchedule(version=1.0):
        from MongoDatabase import MongoDatabase
        return MongoDatabase().getCafeteriaMenu(version)

