from datetime import datetime

from bson import ObjectId

from MongoDatabase import MongoDatabase


class CafeteriaRating:
    def __init__(self):
        pass

    def rateMenu(self, mealId):
        from flask import request
        try:
            #mealId = str(request.values.get("mealid"))
            rating = float(request.values.get("rating"))
        except:
            return "Error: Bad Request. Check parameters."

        if rating > 1 or rating < 0:
            return "Error: Bad Request. rating can be between 0 and 1."

        # if MongoDatabase.getMeal(mealId = mealId) == None:
        #     return "Error: Meal Doesn't Exist."

        remoteIp = request.remote_addr
        MongoDatabase().insertCafeteriaRatingByMealId(ObjectId(mealId), rating, remoteIp, datetime.now())

        return "200"

    def getMealRating(self, mealId=None):
        if mealId:
            try:
                return MongoDatabase().getMealRating(ObjectId(mealId))
            except:
                return 0
        else:
            mealIdAndDates = self._findAllMealIds()
            self._appendMealRatings(mealIdAndDates)
            return mealIdAndDates

    def _findAllMealIds(self):
        import urllib, json
        from Config import Config
        url = Config.cafeteriaServiceUrl + "/allmeals/"
        response = urllib.urlopen(url).read()
        jsonEndpointData = json.loads(response)
        cafeteriaMenuArray = jsonEndpointData['CafeteriaMenu']
        mealsArray = []
        for eachMeal in cafeteriaMenuArray:
            meal = {}
            meal['_id'] = eachMeal['_id']
            meal['startTime'] = eachMeal['startTime']
            mealsArray.append(meal)

        return mealsArray

    def _appendMealRatings(self, mealIdAndDates):
        import urllib, json
        from Config import Config

        for eachMeal in mealIdAndDates:
            url = Config.serverRootLink + "/cafeteria/rating/"+eachMeal['_id']
            response = urllib.urlopen(url)
            jsonEndpointData = json.loads(response.read())
            rating = jsonEndpointData['mealRating']
            eachMeal['rating'] = rating

    def getMealRateCount(self, mealId):
        mealRateCount = MongoDatabase().getMealRateCount(mealId=mealId)
        return mealRateCount

