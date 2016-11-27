class Cafeteria:
    def __init__(self):
        pass

    def getSchedule(self, version):
        from MongoDatabase import MongoDatabase
        return MongoDatabase().getCafeteriaMenu(version if version > 1.0 else 1.0 )

