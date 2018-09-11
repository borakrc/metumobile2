import pymysql.cursors
from Config import Config
from CredentialsConfig import CredentialsConfig


class MetuAcademicAndDormCalendarBridge:
    def __init__(self):
        self.credentials = CredentialsConfig.sinerjiDbCredentials
        self.credentialsNew = CredentialsConfig.newAcademicDbCredentials


    def _connect(self):
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
    def _connectNew(self):
        self.connection = pymysql.connect(
            user=self.credentialsNew.user,
            password=self.credentialsNew.password,
            host=self.credentialsNew.ip,
            db=self.credentialsNew.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )


    def _fetchAll(self):
        self._connect()
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """select
                    e.id,
                    CASE es.sect_id
                    WHEN '36' THEN 'Akademik'
                    else 'Yurt'
                    END as tipi,
                    e.name,
                    e.description,
                    e.date_from,
                    e.date_to
                from
                    b_calendar_event e, b_calendar_event_sect es
                where
                    e.active = 'Y' and
                    e.deleted = 'N' and
                    e.cal_type = 'company_calendar' and
                    e.id = es.event_id and
                    es.sect_id in (36,37) and
                    e.date_to >= CURDATE()
                ORDER BY
                e.date_from
                ASC
                    """
            cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            result = cursor.fetchall()

            announcementsShorterThan6Months = []
            for each in result:
                if not self._isLongerThan6Months(each):
                    each['date_to'] = each['date_to'].isoformat()
                    each['date_from'] = each['date_from'].isoformat()
                    announcementsShorterThan6Months.append(each)
            return announcementsShorterThan6Months
        
    def _fetchAllNew(self):
        self._connectNew()
        
        try:
           c = self.connection.cursor()
        except OperationalError:
           connected = False
            return "false"
        else:
           connected = True
            return "true"
        

    def fetchAcademicAnnouncements(self):
        result = self._fetchAll()
        onlyAcademicAnnouncements = []
        for eachAnnouncement in result:
            if eachAnnouncement['tipi'] == 'Akademik':
                del eachAnnouncement['tipi']
                self._splitTurkishAndEnglish(eachAnnouncement)
                eachAnnouncement['isAllDay'] = self._isAnnouncementAllDay(eachAnnouncement)
                onlyAcademicAnnouncements.append(eachAnnouncement)
        return onlyAcademicAnnouncements
    
    def fetchAcademicAnnouncementsNew(self):
        result = self._fetchAllNew()
        return result
        #onlyAcademicAnnouncements = []
        #for eachAnnouncement in result:
            #self._splitTurkishAndEnglish(eachAnnouncement)
            #eachAnnouncement['isAllDay'] = self._isAnnouncementAllDay(eachAnnouncement)
            #onlyAcademicAnnouncements.append(eachAnnouncement)
        #return onlyAcademicAnnouncements

    def fetchDormAnnouncements(self):
        result = self._fetchAll()
        onlyDormAnnouncements = []
        for eachAnnouncement in result:
            if eachAnnouncement['tipi'] == 'Yurt':
                del eachAnnouncement['tipi']
                self._splitTurkishAndEnglish(eachAnnouncement)
                eachAnnouncement['isAllDay'] = self._isAnnouncementAllDay(eachAnnouncement)
                onlyDormAnnouncements.append(eachAnnouncement)
        return onlyDormAnnouncements

    def _isLongerThan6Months(self, event):
        firstDate = event['date_from']
        lastDate = event['date_to']
        delta = lastDate - firstDate
        return True if delta.days>180 else False

    def _splitTurkishAndEnglish(self, eachAnnouncement):
        nOfSplitters = self._countNumberOfSplitters(eachAnnouncement['name'])
        if nOfSplitters % 2 == 0:
            eachAnnouncement['en_name'] = eachAnnouncement['name']
            eachAnnouncement['tr_name'] = eachAnnouncement['name']
            return
        announcementNameArray = eachAnnouncement['name'].split('/')
        tr_annNameArray = announcementNameArray[(nOfSplitters/2)+1:]
        en_annNameArray = announcementNameArray[0:nOfSplitters/2+1]

        tr_annName = ""
        for each in tr_annNameArray:
            tr_annName += each + "/"
        tr_annName = tr_annName[:-1]

        en_annName = ""
        for each in en_annNameArray:
            en_annName += each + "/"
        en_annName = en_annName[:-1]

        eachAnnouncement['tr_name'] = tr_annName
        eachAnnouncement['en_name'] = en_annName

        return
    


    def _countNumberOfSplitters(self, param):
        return param.count('/')

    def _isAnnouncementAllDay(self, announcement):
        try:
            firstDate = announcement['date_from']
            lastDate = announcement['date_to']

            delta = lastDate - firstDate
            if delta.hours > 23:
                return True
            if firstDate.hours == 0 and firstDate.minutes == 0 and firstDate.seconds == 0:
                return True
        except:
            pass

        return False






