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
            sql = "select distinct end_date, en_type from alacarte_menu where end_date >= NOW() order by id asc"
           
            cursor.execute(sql)
            
            self.connection.commit()
            all_dates = cursor.fetchall()
            
            jsonableArray = []
            for each_date in all_dates:

                sql = "select * from alacarte_menu where end_date = '" + each_date['end_date'].isoformat() + "' and en_type='" + each_date['en_type']+ "' order by id asc"
                
                cursor.execute(sql)

                self.connection.commit()
                all_meal = cursor.fetchall()
                
                meal={}
                
                meal['details']={}
                for each_meal in all_meal:
                    
                    meal['id'] = str(each_meal['id'])
                    meal['start_date'] = (each_meal['start_date']).isoformat()
                    meal['end_date'] = (each_meal['end_date']).isoformat()
                    meal['type_en'] = (each_meal['en_type'])
                    meal['type_tr'] = (each_meal['tr_type'])
                    
                    if each_meal['food_type'] == 'soup':
                        meal['details']['soup']={}
                        meal['details']['soup']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['soup']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['soup']['calorie']=each_meal['calorie']
                        meal['details']['soup']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'main1': 
                        meal['details']['main1']={}
                        meal['details']['main1']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['main1']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['main1']['calorie']=each_meal['calorie']
                        meal['details']['main1']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'main2':
                        meal['details']['main2']={}
                        meal['details']['main2']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['main2']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['main2']['calorie']=each_meal['calorie']
                        meal['details']['main2']['protein']=each_meal['protein'] 
                    elif each_meal['food_type'] == 'vegeterian':
                        meal['details']['vegeterian']={}
                        meal['details']['vegeterian']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['vegeterian']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['vegeterian']['calorie']=each_meal['calorie']
                        meal['details']['vegeterian']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'sider1':                        
                        meal['details']['sider1']={}
                        meal['details']['sider1']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['sider1']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['sider1']['calorie']=each_meal['calorie']
                        meal['details']['sider1']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'sider2':                        
                        meal['details']['sider2']={}
                        meal['details']['sider2']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['sider2']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['sider2']['calorie']=each_meal['calorie']
                        meal['details']['sider2']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'sider3':                        
                        meal['details']['sider3']={}
                        meal['details']['sider3']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['sider3']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['sider3']['calorie']=each_meal['calorie']
                        meal['details']['sider3']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'extra':                        
                        meal['details']['extra']={}
                        meal['details']['extra']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal['details']['extra']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal['details']['extra']['calorie']=each_meal['calorie']
                        meal['details']['extra']['protein']=each_meal['protein']
                jsonableArray.append(meal)
                        
               
            return jsonableArray
    
    def setAlacarteMenu(self, allMealsInFile):
        self._connect()
        AlacarteBridge.lastImportedAlacarteMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO cafeteria.alacarte_menu_tester (tr_type, en_type, start_date, end_date, tr_name, en_name, calorie, protein, food_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE tr_name = %s, en_name=%s, (eachMeal['tr_type'], eachMeal['en_type'], eachMeal['startTime'], eachMeal['endTime'], eachMeal['tr_name'], eachMeal['en_name'], eachMeal['calorie'], eachMeal['protein'], eachMeal['food_type'], eachMeal['startTime'], eachMeal['food_type']))

                self.connection.commit()
    
