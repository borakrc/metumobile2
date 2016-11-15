from datetime import datetime
from bson import ObjectId
from MongoDatabase import MongoDatabase
from hashlib import md5


class CafeteriaRating:
    def __init__(self):
        pass

    def rateMenu(self, mealId):
        from flask import request
        try:
            #mealId = str(request.values.get("mealid"))
            rating = float(request.values.get("rating"))
        except Exception:
            return "Error: Bad Request. Check parameters."
        if rating > 1 or rating < 0:
            return "Error: Bad Request. rating can be between 0 and 1."

        # if MongoDatabase.getMeal(mealId = mealId) == None:
        #     return "Error: Meal Doesn't Exist."

        remoteIp = md5(request.remote_addr).hexdigest()
        MongoDatabase().insertCafeteriaRatingByMealId(
                ObjectId(mealId), rating, remoteIp, datetime.now()
        )
        return "200"

    def getMealRating(self, mealId):
        try:
            return MongoDatabase().getMealRating(ObjectId(mealId))
        except:
            return 0
