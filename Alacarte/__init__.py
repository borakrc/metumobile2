from MysqlDatabase import MysqlDatabase


class Alacarte:
    def __init__(self):
        pass

    def getUpcomingAlacarte(self, version):
        return MysqlDatabase().getUpcomingAlacarteMenu(version if version >= 1.1 else 1.0)

    def getAllMeals(self):
        return MongoDatabase().getAllCafeteriaMenu()

    def expandRatingsWithMeal(self, mealRatings):
        for meal in mealRatings:
            mealId = meal['_id']

            import urllib, json
            from Config import Config
            url = Config.cafeteriaServiceUrl + "/meals/"+mealId
            response = urllib.urlopen(url).read()
            jsonEndpointData = json.loads(response)
            mealDetails = jsonEndpointData
            meal['tr_name'] = mealDetails['tr_name']
            meal['dishes.main.tr_name'] = mealDetails['dishes']['main']['tr_name']
            meal['dishes.side.tr_name'] = mealDetails['dishes']['side']['tr_name']
            meal['dishes.soup.tr_name'] = mealDetails['dishes']['soup']['tr_name']

        return mealRatings

    def getMeal(self, mealId):
        meal = MongoDatabase().getMeal(mealId=mealId)
        return meal
