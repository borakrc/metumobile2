from MetuAnnouncementsBridge import MetuAcademicAndDormCalendarBridge

class Announcements:
    def fetchCategory(self, categoryId):
        return self._fetchStaticAnnouncementCategory(categoryId)

    def _fetchStaticAnnouncementCategory(self, categoryId):
        if categoryId == 0:
            answerDictionary = {}
            answerDictionary['announcements'] = MetuAcademicAndDormCalendarBridge().fetchAcademicAnnouncements()
            answerDictionary['isActive'] = True
            answerDictionary['en_name'] = "Academic"
            answerDictionary['tr_name'] = "Akademik"
        elif categoryId == 1:
            answerDictionary = {}
            answerDictionary['announcements'] = MetuAcademicAndDormCalendarBridge().fetchDormAnnouncements()
            answerDictionary['isActive'] = True
            answerDictionary['en_name'] = "Dormitories"
            answerDictionary['tr_name'] = "Yurtlar"
        else:
            answerDictionary = {}
            answerDictionary['announcements'] = []
            answerDictionary['isActive'] = False
            answerDictionary['en_name'] = "Other Category(Passive)"
            answerDictionary['tr_name'] = "Diger Kategori(Pasif)"
        answerDictionary['_id'] = categoryId
        return answerDictionary
