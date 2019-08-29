import pymysql.cursors
from Cafeteria.MealContainer import MealContainer
from Alacarte.AlacarteMealContainer import AlacarteMealContainer
from CredentialsConfig import CredentialsConfig


class MysqlDatabase:
    def __init__(self):
        self.credentials = CredentialsConfig.mysqlDbCredentials
        try:
            self._connect()
        except:
            print ("MySql connection failed.")

    def _connect(self):
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True)
        self.cursor = self.connection.cursor()
        
    def getUpcomingAlacarteMenu(self, version):
        from datetime import datetime
        mycursor = mydb.cursor()

        sql="select * from alacarte_menu where end_date > NOW()"
        
        myresult=self.cursor.execute(sql)
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
        
        
    def setCafeteriaMenu(self, mealArray):
        for eachMeal in mealArray:
            assert isinstance(eachMeal, MealContainer)
            self._upsertMeal(eachMeal)

    def setAlacarteMenu(self, mealArray):
        for eachMeal in mealArray:
            assert isinstance(eachMeal, AlacarteMealContainer)
            self._uploadAlacarteMeal(eachMeal)
    
    def _uploadAlacarteMeal(self, meal):
        assert isinstance(meal, AlacarteMealContainer)
        
        #sqlVariables = meal.serialize() + meal.serialize()
        #placeholders = ', '.join(['%s'] * len(sqlVariables))  # "%s, %s, %s, ... %s"
        
        sql = """INSERT INTO cafeteriaMenu (
                activeUntilDate,
                en_name,
                tr_name,
                startDate,
                endDate,
                en_mainDish,
                en_sideDish,
                en_soup,
                en_extra1,
                en_extra2,
                en_extra3,
                tr_mainDish,
                tr_sideDish,
                tr_soup,
                tr_extra1,
                tr_extra2,
                tr_extra3
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON DUPLICATE KEY UPDATE
                activeUntilDate=?,
                en_name=?,
                tr_name=?,
                startDate=?,
                endDate=?,
                en_mainDish=?,
                en_sideDish=?,
                en_soup=?,
                en_extra1=?,
                en_extra2=?,
                en_extra3=?,
                tr_mainDish=?,
                tr_sideDish=?,
                tr_soup=?,
                tr_extra1=?,
                tr_extra2=?,
                tr_extra3=?
        """

        #self.cursor.execute(sql, sqlVariables)
        #self.connection.commit()

        return
    
    
    def _upsertMeal(self, meal):
        assert isinstance(meal, MealContainer)
        
        sqlVariables = meal.serialize() + meal.serialize()
        #placeholders = ', '.join(['%s'] * len(sqlVariables))  # "%s, %s, %s, ... %s"
        
        sql = """INSERT INTO cafeteriaMenu (
                activeUntilDate,
                en_name,
                tr_name,
                startDate,
                endDate,
                en_mainDish,
                en_sideDish,
                en_soup,
                en_extra1,
                en_extra2,
                en_extra3,
                tr_mainDish,
                tr_sideDish,
                tr_soup,
                tr_extra1,
                tr_extra2,
                tr_extra3
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON DUPLICATE KEY UPDATE
                activeUntilDate=?,
                en_name=?,
                tr_name=?,
                startDate=?,
                endDate=?,
                en_mainDish=?,
                en_sideDish=?,
                en_soup=?,
                en_extra1=?,
                en_extra2=?,
                en_extra3=?,
                tr_mainDish=?,
                tr_sideDish=?,
                tr_soup=?,
                tr_extra1=?,
                tr_extra2=?,
                tr_extra3=?
        """

        self.cursor.execute(sql, sqlVariables)
        self.connection.commit()

        return
