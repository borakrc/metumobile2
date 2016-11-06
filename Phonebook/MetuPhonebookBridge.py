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


