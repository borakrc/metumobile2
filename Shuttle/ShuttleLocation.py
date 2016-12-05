import pymysql.cursors

from CredentialsConfig import CredentialsConfig


class ShuttleLocation:
    def __init__(self):
        self.credentials = CredentialsConfig.shuttleGpsDbCredentials


    def _connect(self):
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)


    def fetchAll(self):
        self._connect()
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """select
                    *
                from
                    positions
                where
                    deviceid = 2 AND
                    id = (
                                SELECT max(id) FROM positions where deviceid = 2
                                )
                    """
            cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            sqlresult = cursor.fetchone()
            #print result

            result = {}
            result['latitude'] = sqlresult['latitude']
            result['longitude'] = sqlresult['longitude']
            result['updatetime'] = sqlresult['devicetime'].isoformat()

            self.connection.close()

            if self._isOutOfRange(result):
                result['latitude'] = 35.249005
                result['longitude'] = 33.022165

            return (result)

    def _isOutOfRange(self, result):
        if result['latitude'] < 35.181790 and result['longitude'] > 33.000766:
            return True
        else:
            return False

    def raw(self):
        self._connect()
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """select * from positions order by id desc limit 500"""

            cursor.execute(sql)

            self.connection.commit()
            resultArray = []
            for each in cursor.fetchall():
                resultArray.append(each)
            return resultArray

    def multipleshuttles(self):
        self._connect()
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """select
                        max(id) as id
                    from
                        positions
                    group by deviceid"""

            cursor.execute(sql)
            self.connection.commit()
            idArray = []
            for mostRecentUpdatedIdForEachDevice in cursor.fetchall():
                id = int(mostRecentUpdatedIdForEachDevice['id'])
                idArray.append(id)

            refinedList = ','.join(str(a) for a in idArray)

            sql = """select
                id, latitude, longitude, devicetime, deviceid
                from positions
                where id in (%s)""" % refinedList

            cursor.execute(sql)
            self.connection.commit()

            locationArray = []

            for location in cursor.fetchall():
                location['updatetime'] = location['devicetime']
                del location['devicetime']
                location['isActive'] = True
                isUpToDate = self._checkIsLastUpdateTimeBiggerThanMinutes(15, location)
                if isUpToDate is True:
                    pass
                else:
                    location['updatetime'] = location['updatetime'].isoformat()
                    locationArray.append(location)

            resultDict = {}
            resultDict['isActive'] = True
            resultDict['locationArray'] = locationArray
            return resultDict

    def _checkIsLastUpdateTimeBiggerThanMinutes(self, minutes, location):
        lastUpdateTime = location['updatetime']
        import datetime
        timeDifference = lastUpdateTime - datetime.datetime.now()
        if timeDifference.min > minutes:
            return True
        else:
            return False
