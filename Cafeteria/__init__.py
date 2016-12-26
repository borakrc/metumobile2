from MongoDatabase import MongoDatabase


class Cafeteria:
    def __init__(self):
        pass

    def getUpcomingSchedule(self, version):
        return MongoDatabase().getUpcomingCafeteriaMenu(version if version >= 1.1 else 1.0)

    def getAllMeals(self):
        return MongoDatabase().getAllCafeteriaMenu()

    def expandRatingsWithMeal(self, mealRatings):
        for meal in mealRatings:
            mealId = meal['_id']
            mealDetails = MongoDatabase().getMeal(mealId=mealId)
            meal['tr_name'] = mealDetails['tr_name']
            meal['dishes.main.tr_name'] = mealDetails['dishes']['main']['tr_name']
            meal['dishes.side.tr_name'] = mealDetails['dishes']['side']['tr_name']
            meal['dishes.soup.tr_name'] = mealDetails['dishes']['soup']['tr_name']

        return mealRatings





