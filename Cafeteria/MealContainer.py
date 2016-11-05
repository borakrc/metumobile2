class MealContainer:
    def __init__(self, date, mealDetailsContainer):
        self.date = date
        self.details = mealDetailsContainer

    def serialize(self):
        return (
            [self.date] +
            self.details.serialize()
        )

    def toJson(self):
        jsonified = self.__dict__
        jsonified['details'] = jsonified['details'].toJson()
        return jsonified

