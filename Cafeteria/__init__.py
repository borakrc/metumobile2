class Cafeteria:
    def __init__(self):
        pass

    @staticmethod
    def getSchedule():
        from MongoDatabase import MongoDatabase
        return MongoDatabase().getCafeteriaMenu()

