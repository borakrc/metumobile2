import pymysql.cursors

from CredentialsConfig import CredentialsConfig


class AlacarteBridge:
    lastImportedAlacarteMenu = []
    def __init__(self):
        self.credentials = CredentialsConfig.alacarteRestaurantCredentials

    def _connect(self):
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    
    def getUpcomingAlacarteMenu(self, version):
        self._connect()
        with self.connection.cursor() as cursor:
            sql = "select * from alacarte_menu where end_date > NOW()"
           
            cursor.execute(sql)
            
            self.connection.commit()
            myresult = cursor.fetchall()
        
        #self.cursor.execute("select * from alacarte_menu where end_date > NOW()")

        jsonableArray = []
        for each in myresult:
            meal = {}
            meal['id'] = str(each['id'])
            meal['tr_type'] = each['tr_type']
            meal['en_type'] = each['en_type']
            meal['start_date'] = each['start_date']
            meal['end_date'] = each['end_date']
            meal['tr_name'] = each['tr_name']
            meal['en_name'] = each['en_name']
            meal['calorie'] = each['calorie']
            meal['protein'] = each['protein']
            meal['food_type'] = each['food_type']
            jsonableArray.append(meal)

        return jsonableArray
    
    def setAlacarteMenu(self, allMealsInFile):
        AlacarteBridge.lastImportedAlacarteMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO cafeteria.alacarte_menu (tr_type, en_type, start_date, end_date, tr_name, en_name, calorie, protein, food_type) values (?,?,?,?,?,?,?,?,?)', (eachMeal['tr_type'], eachMeal['en_type'], eachMeal['start_date'], eachMeal['end_date'], eachMeal['tr_name'], eachMeal['en_name'], eachMeal['calorie'], eachMeal['protein'], eachMeal['food_type']))

                self.connection.commit()
    


