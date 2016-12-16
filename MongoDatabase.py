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

    def getUpcomingCafeteriaMenu(self, version):
        if version == 1.0:
            from datetime import datetime
            results = self.db['cafeteriaMenu'].find({"endTime": {"$gt": datetime.now()}})
            jsonableArray = []
            for each in results:
                each['endTime'] = each['endTime'].isoformat()
                each['startTime'] = each['startTime'].isoformat()
                each['_id'] = str(each['_id'])

                mealInOldFormat = self._convertNewMealToOldMeal(each)

                jsonableArray.append(mealInOldFormat)
            return jsonableArray
        else:
            from datetime import datetime
            #results = self.db['cafeteriaMenu'].find({})
            results = self.db['cafeteriaMenu'].find({"endTime": {"$gt": datetime.now()}})
            jsonableArray = []
            for each in results:
                each['endTime'] = each['endTime'].isoformat()
                each['startTime'] = each['startTime'].isoformat()
                each['_id'] = str(each['_id'])
                jsonableArray.append(each)
            return jsonableArray


    def setCafeteriaMenu(self, allMealsInFile):
        MongoDatabase.lastImportedCafeteriaMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            self.db['cafeteriaMenu'].update({'endTime':eachMeal['endTime']}, eachMeal, upsert=True)



    def insertCafeteriaRating(self, day, month, year, dinnerName, rating, remoteIp, datetime):
        self.db['cafeteriaRating'].insert({'day':day, 'month':month, 'year':year, 'dinnerName':dinnerName, 'rating':rating, 'remoteIp':remoteIp, 'lastUpdateTime': datetime})

    def insertCafeteriaRatingByMealId(self, mealId, rating, remoteIp, datetime):
        self.db['cafeteriaRating'].insert({'mealId':mealId, 'rating':rating, 'remoteIp':remoteIp, 'lastUpdateTime': datetime})

    def getMealRating(self, mealId):
        results = self.db['cafeteriaRating'].find({"mealId": mealId})
        jsonableArray = []
        _sum, index = 0, 0  # if results empty
        for index, each in enumerate(results):
            _sum += each['rating']
        return float(_sum) / (index+1)

    def getMeal(self, mealId):
        raise NotImplementedError

    def _convertNewMealToOldMeal(self, newMeal):
        oldMeal = {}
        oldMeal['_id'] = newMeal['_id']
        oldMeal['date'] = newMeal['endTime']
        oldMeal['details'] = {}

        oldMeal['details']['en_menu'] = {}
        oldMeal['details']['en_menu']['main'] = newMeal['dishes']['main']['en_name']
        oldMeal['details']['en_menu']['pastaOrRice'] = newMeal['dishes']['side']['en_name']
        oldMeal['details']['en_menu']['soup'] = newMeal['dishes']['soup']['en_name']
        oldMeal['details']['en_menu']['extras'] = [newMeal['dishes']['extras'][0]['en_name'],
                                                   newMeal['dishes']['extras'][1]['en_name']]

        oldMeal['details']['tr_menu'] = {}
        oldMeal['details']['tr_menu']['main'] = newMeal['dishes']['main']['tr_name']
        oldMeal['details']['tr_menu']['pastaOrRice'] = newMeal['dishes']['side']['tr_name']
        oldMeal['details']['tr_menu']['soup'] = newMeal['dishes']['soup']['tr_name']
        oldMeal['details']['tr_menu']['extras'] = [newMeal['dishes']['extras'][0]['tr_name'],
                                                   newMeal['dishes']['extras'][1]['tr_name']]

        oldMeal['details']['en_name'] = newMeal['en_name']
        oldMeal['details']['tr_name'] = newMeal['tr_name']
        oldMeal['details']['end'] = newMeal['endTime']
        oldMeal['details']['start'] = newMeal['startTime']

        return oldMeal

    def getAllCafeteriaMenu(self):
        results = self.db['cafeteriaMenu'].find({})
        jsonableArray = []
        for each in results:
            try:
                each['endTime'] = each['endTime'].isoformat()
                each['startTime'] = each['startTime'].isoformat()
                each['_id'] = str(each['_id'])
                jsonableArray.append(each)
            except:
                pass
        return jsonableArray

