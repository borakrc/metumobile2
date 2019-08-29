import pymysql.cursors

from CredentialsConfig import CredentialsConfig


class PhonebookBridge:
    def __init__(self):
        self.credentials = CredentialsConfig.phonebookDbCredentials

    def _connect(self):
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    def fetchAllFromDb(self):
        self._connect()
        with self.connection.cursor() as cursor:
            sql = """select *
              from rehber
              ORDER BY name ASC"""
            #where durum not like '%pasif%'"""
            cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            result = cursor.fetchall()
            return result

        
    def getUpcomingAlacarteMenu(self, version):
        self._connect()
        with self.connection.cursor() as cursor:
            sql = "select * from alacarte_menu where end_date > NOW()"
           
            cursor.execute(sql)
            
            self.connection.commit()
            result = cursor.fetchall()
        
        #self.cursor.execute("select * from alacarte_menu where end_date > NOW()")

        myresult = self.cursor.fetchall()

        jsonableArray = []
        for each in myresult:

            meal['id'] = str(each['id'])
            meal['tr_type'] = str(each['tr_type'])
            meal['en_type'] = str(each['en_type'])
            meal['start_date'] = each['start_date'].isoformat()
            meal['end_date'] = each['end_date'].isoformat()
            meal['tr_name'] = str(each['tr_name'])
            meal['en_name'] = str(each['en_name'])
            meal['calorie'] = str(each['calorie'])
            meal['protein'] = str(each['protein'])
            meal['food_type'] = str(each['food_type'])
            jsonableArray.append(meal)

        return jsonableArray


