from Cafeteria.MealContainer import MealContainer
from Config import Config
from CredentialsConfig import CredentialsConfig

class MongoDatabase:
    lastImportedCafeteriaMenu = []

    def __init__(self):
        self.credentials = CredentialsConfig.mongoDbCredentials
        try:
            from datetime import datetime
            from pymongo import MongoClient
            if Config.os == 'Windows':
                pass
            else:
                self.client = MongoClient(self.credentials.ip)
                self.db = self.client.admin
                self.db.authenticate(self.credentials.user, self.credentials.password)#
                self.db = self.client.metumobile
            print ("db connection successful! " + str(datetime.now()))
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
            self.db['cafeteriaMenu'].update({'date':eachMeal.date}, eachMeal.toJson(), upsert=True)

    # TODO refactor the next 3 functions!
    def insertCafeteriaRating(self, day, month, year, dinnerName, rating, remoteIp, datetime):
        self.db['cafeteriaRating'].insert({'day':day, 'month':month, 'year':year, 'dinnerName':dinnerName, 'rating':rating, 'remoteIp':remoteIp, 'lastUpdateTime': datetime})

    def insertCafeteriaRatingByMealId(self, mealId, rating, remoteIp, datetime):
        self.db['cafeteriaRating'].insert({'mealId':mealId, 'rating':rating, 'remoteIp':remoteIp, 'lastUpdateTime': datetime})

    def insertCafeteriaRatingCommentByMealId(self, mealId, rating,
                                             remoteIp, datetime, comment):
        self.db['cafeteriaRating'].insert({
            'mealId': mealId, 'rating': rating, 'remoteIp': remoteIp,
            'lastUpdateTime': datetime, "comment": comment
            })

    def getMealRating(self, mealId):
        results = self.db['cafeteriaRating'].find({"mealId": mealId})
        jsonableArray = []
        _sum, index = 0, 0  # if results empty
        for index, each in enumerate(results):
            _sum += each['rating']
        return float(_sum) / (index+1)

    def getMeal(self, mealId):
        raise NotImplementedError
