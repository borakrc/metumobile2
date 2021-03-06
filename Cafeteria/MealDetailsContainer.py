from datetime import datetime

from Cafeteria.MealMenuContainer import MealMenuContainer


class MealDetailsContainer(object):
    def __init__(self, start,
                 end,
                 en_name,
                 tr_name,
                 en_menu,
                 tr_menu):
        assert isinstance(start, datetime)
        assert isinstance(end, datetime)
        self.start = start
        self.end = end
        self.en_name = en_name
        self.tr_name = tr_name
        assert isinstance(en_menu, MealMenuContainer)
        assert isinstance(tr_menu, MealMenuContainer)
        self.en_menu = en_menu
        self.tr_menu = tr_menu

    def serialize(self):
        en_menu = self.en_menu.serialize()
        tr_menu = self.tr_menu.serialize()
        assert isinstance(en_menu,list)
        assert isinstance(tr_menu,list)
        return (
            [
            self.en_name,
            self.tr_name,
            self.start,
            self.end]+
            en_menu+
            tr_menu
        )

    def toJson(self):
        jsonified = self.__dict__
        jsonified['en_menu'] = jsonified['en_menu'].toJson()
        jsonified['tr_menu'] = jsonified['tr_menu'].toJson()
        return jsonified