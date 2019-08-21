class AlacarteMealMenuContainer(object):

    def __init__(self, main, pastaOrRice, soup, extra1=None, extra2=None, extra3=None):
        self.main = main
        self.pastaOrRice = pastaOrRice
        self.soup = soup
        self.extra1 = extra1
        self.extra2 = extra2
        self.extra3 = extra3

    def serialize(self):
        return ([
            self.main,
            self.pastaOrRice,
            self.soup,
            self.extra1,
            self.extra2,
            self.extra3
            ]
        )

    def toJson(self):
        dictVersion = self.__dict__
        dictVersion['extras'] = [self.extra1, self.extra2, self.extra3]
        dictVersion['extras'].remove(None)
        return dictVersion
