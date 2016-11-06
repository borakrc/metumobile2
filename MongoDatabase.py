from Cafeteria.MealContainer import MealContainer
from Config import Config
from CredentialsConfig import CredentialsConfig

class MongoDatabase:
    lastImportedCafeteriaMenu = []

    def __init__(self):
        self.credentials = CredentialsConfig.mongoDbCredentials
        try:
            from pymongo import MongoClient
            if Config.os == 'Windows':
                pass
            else:
                self.client = MongoClient(self.credentials.ip)
                self.db = self.client.admin
                self.db.authenticate(self.credentials.user, self.credentials.password)#
                self.db = self.client.metumobile
        except:
            print ("db connection failed!")
            self.client.close()

    def getCafeteriaMenu(self):
        from datetime import datetime
        results = self.db['cafeteriaMenu'].find({"details.end": {"$gt": datetime.now()}})
        jsonableArray = []
        for each in results:
            each['date'] = each['date'].isoformat()
            each['details']['start'] = each['details']['start'].isoformat()
            each['details']['end'] = each['details']['end'].isoformat()
            each['_id'] = str(each['_id'])
            jsonableArray.append(each)
        return jsonableArray


    def setCafeteriaMenu(self, allMealsInFile):
        MongoDatabase.lastImportedCafeteriaMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            assert isinstance(eachMeal, MealContainer)
            try:
                self.db['cafeteriaMenu'].update({'date':eachMeal.date}, eachMeal.toJson(), upsert=True)
            except Exception:
                print "Encountered error during database write."
                import traceback
                print traceback.format_exc()


    def insertCafeteriaRating(self, day, month, year, dinnerName, rating, remoteIp, datetime):
        self.db['cafeteriaRating'].insert({'day':day, 'month':month, 'year':year, 'dinnerName':dinnerName, 'rating':rating, 'remoteIp':remoteIp, 'lastUpdateTime': datetime})

    def insertCafeteriaRatingByMealId(self, mealId, rating, remoteIp, datetime):
        self.db['cafeteriaRating'].insert({'mealId':mealId, 'rating':rating, 'remoteIp':remoteIp, 'lastUpdateTime': datetime})

    def getMealRating(self, mealId):
        results = self.db['cafeteriaRating'].find({"mealId": mealId})
        jsonableArray = []
        sum = 0
        count = 0
        for each in results:
            sum += each['rating']
            count += 1
        try:
            average = float(sum) / count
        except:
            return 0
        return average

    def getMeal(self, mealId):
        raise NotImplementedError
