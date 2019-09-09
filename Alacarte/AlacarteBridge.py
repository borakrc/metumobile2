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

                sql = "select * from alacarte_menu where end_date = '" + each_date['end_date'] + "' and en_type='" + each_date['en_type']+ "' order by id asc"
                
                cursor.execute(sql)

                self.connection.commit()
                all_meal = cursor.fetchall()
                
                meal={}
                
                meal[each_date['en_type']]={}
                for each_meal in all_meal:
                    text_file = open("console.txt", "w")
                    text_file.write("food_type: %s\n" % each_meal['food_type'])
                    text_file.write("tr_name: %s\n" % each_meal['tr_name'].encode('utf-8'))
                    text_file.write("en_name: %s\n" % each_meal['en_name'])
                    text_file.write("calorie: %s\n" % each_meal['calorie'])
                    text_file.write("protein: %s\n" % each_meal['protein'])
                    text_file.close()
                    meal['start'] = (each_meal['start_date'])
                    meal['end'] = (each_meal['end_date'])
                    if each_meal['food_type'] == 'soup':
                        meal[each_date['en_type']]['soup']={}
                        meal[each_date['en_type']]['soup']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['soup']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['soup']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['soup']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'main1': 
                        meal[each_date['en_type']]['main1']={}
                        meal[each_date['en_type']]['main1']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['main1']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['main1']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['main1']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'main2':
                        meal[each_date['en_type']]['main2']={}
                        meal[each_date['en_type']]['main2']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['main2']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['main2']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['main2']['protein']=each_meal['protein'] 
                    elif each_meal['food_type'] == 'vegeterian':
                        meal[each_date['en_type']]['vegeterian']={}
                        meal[each_date['en_type']]['vegeterian']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['vegeterian']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['vegeterian']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['vegeterian']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'sider1':                        
                        meal[each_date['en_type']]['sider1']={}
                        meal[each_date['en_type']]['sider1']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['sider1']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['sider1']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['sider1']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'sider2':                        
                        meal[each_date['en_type']]['sider2']={}
                        meal[each_date['en_type']]['sider2']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['sider2']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['sider2']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['sider2']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'sider3':                        
                        meal[each_date['en_type']]['sider3']={}
                        meal[each_date['en_type']]['sider3']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['sider3']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['sider3']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['sider3']['protein']=each_meal['protein']
                    elif each_meal['food_type'] == 'extra':                        
                        meal[each_date['en_type']]['extra']={}
                        meal[each_date['en_type']]['extra']['tr_name']=(each_meal['tr_name']).encode('utf-8')
                        meal[each_date['en_type']]['extra']['en_name']=(each_meal['en_name']).encode('utf-8')
                        meal[each_date['en_type']]['extra']['calorie']=each_meal['calorie']
                        meal[each_date['en_type']]['extra']['protein']=each_meal['protein']
                jsonableArray.append(meal)
                        
               
            return jsonableArray
    
    def setAlacarteMenu(self, allMealsInFile):
        self._connect()
        AlacarteBridge.lastImportedAlacarteMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO cafeteria.alacarte_menu (tr_type, en_type, start_date, end_date, tr_name, en_name, calorie, protein, food_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (eachMeal['tr_type'], eachMeal['en_type'], eachMeal['startTime'], eachMeal['endTime'], eachMeal['tr_name'], eachMeal['en_name'], eachMeal['calorie'], eachMeal['protein'], eachMeal['food_type']))

                self.connection.commit()
    
