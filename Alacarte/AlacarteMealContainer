from AlacarteMealDetailsContainer import AlacarteMealDetailsContainer


class AlacarteMealContainer:
    def __init__(self, date, alacarteMealDetailsContainer):
        self.date = date
        assert isinstance(alacarteMealDetailsContainer, AlacarteMealDetailsContainer)
        self.details = alacarteMealDetailsContainer

    def serialize(self):
        return (
            [self.date] +
            self.details.serialize()
        )

    def toJson(self):
        jsonified = self.__dict__
        jsonified['details'] = jsonified['details'].toJson()
        return jsonified
