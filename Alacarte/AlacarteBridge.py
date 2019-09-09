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
            sql = "select distinct end_date from alacarte_menu where end_date >= NOW() order by id asc"
           
            cursor.execute(sql)
            
            self.connection.commit()
            all_dates = cursor.fetchall()
            
            jsonableArray = []
            for each_date in all_dates:

                sql = "select * from alacarte_menu where end_date = '" + each_date['end_date'] + "' and en_type='Lunch' order by id asc"
                
                cursor.execute(sql)

                self.connection.commit()
                all_lunch = cursor.fetchall()
                
                
                
                
               
                
                lunches={}
                for each_lunch in all_lunch:
                    
                    
                    text_file = open("console.txt", "w")
                    text_file.write("food_type: %s\n" % each_lunch['food_type'])
                    text_file.write("tr_name: %s\n" % each_lunch['tr_name'].encode('utf-8'))
                    text_file.write("en_name: %s\n" % each_lunch['en_name'])
                    text_file.write("calorie: %s\n" % each_lunch['calorie'])
                    text_file.write("protein: %s\n" % each_lunch['protein'])
                    text_file.close()
                    
                    if each_lunch['food_type'] == 'soup':
                        lunches['soup']={}
                        lunches['soup']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['soup']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['soup']['calorie']=each_lunch['calorie']
                        lunches['soup']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'main1': 
                        lunches['main1']={}
                        lunches['main1']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['main1']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['main1']['calorie']=each_lunch['calorie']
                        lunches['main1']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'main2':
                        lunches['main2']={}
                        lunches['main2']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['main2']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['main2']['calorie']=each_lunch['calorie']
                        lunches['main2']['protein']=each_lunch['protein'] 
                    elif each_lunch['food_type'] == 'vegeterian':
                        lunches['vegeterian']={}
                        lunches['vegeterian']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['vegeterian']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['vegeterian']['calorie']=each_lunch['calorie']
                        lunches['vegeterian']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider1':                        
                        lunches['sider1']={}
                        lunches['sider1']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['sider1']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['sider1']['calorie']=each_lunch['calorie']
                        lunches['sider1']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider2':                        
                        lunches['sider2']={}
                        lunches['sider2']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['sider2']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['sider2']['calorie']=each_lunch['calorie']
                        lunches['sider2']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider3':                        
                        lunches['sider3']={}
                        lunches['sider3']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['sider3']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['sider3']['calorie']=each_lunch['calorie']
                        lunches['sider3']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'extra':                        
                        lunches['extra']={}
                        lunches['extra']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['extra']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['extra']['calorie']=each_lunch['calorie']
                        lunches['extra']['protein']=each_lunch['protein']
                jsonableArray.append(lunches)
                        
                sql = "select * from alacarte_menu where end_date = '" + each_date['end_date'] + "' and en_type='Dinner' order by id asc"
                
                cursor.execute(sql)

                self.connection.commit()
                all_dinner = cursor.fetchall()
                
                dinners={}
                for each_dinner in all_dinner:
                    
                    text_file = open("console.txt", "w")
                    text_file.write("food_type: %s\n" % each_dinner['food_type'])
                    text_file.write("tr_name: %s\n" % each_dinner['tr_name'].encode('utf-8'))
                    text_file.write("en_name: %s\n" % each_dinner['en_name'])
                    text_file.write("calorie: %s\n" % each_dinner['calorie'])
                    text_file.write("protein: %s\n" % each_dinner['protein'])
                    text_file.close()
                    
                    if each_dinner['food_type'] == 'soup':
                        dinners['soup']={}              
                        dinners['soup']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['soup']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['soup']['calorie']=each_dinner['calorie']
                        dinners['soup']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'main1': 
                        dinners['main1']={}
                        dinners['main1']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['main1']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['main1']['calorie']=each_dinner['calorie']
                        dinners['main1']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'main2':
                        dinners['main2']={}
                        dinners['main2']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['main2']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['main2']['calorie']=each_dinner['calorie']
                        dinners['main2']['protein']=each_dinner['protein'] 
                    elif each_dinner['food_type'] == 'vegeterian':
                        dinners['vegeterian']={}
                        dinners['vegeterian']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['vegeterian']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['vegeterian']['calorie']=each_dinner['calorie']
                        dinners['vegeterian']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'sider1':                        
                        dinners['sider1']={}
                        dinners['sider1']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['sider1']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['sider1']['calorie']=each_dinner['calorie']
                        dinners['sider1']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'sider2':                        
                        dinners['sider2']={}
                        dinners['sider2']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['sider2']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['sider2']['calorie']=each_dinner['calorie']
                        dinners['sider2']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'sider3':
                        dinners['sider3']={}
                        dinners['sider3']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['sider3']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['sider3']['calorie']=each_dinner['calorie']
                        dinners['sider3']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'extra':                        
                        dinners['extra']={}
                        dinners['extra']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['extra']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['extra']['calorie']=each_dinner['calorie']
                        dinners['extra']['protein']=each_dinner['protein']
                        
                jsonableArray.append(dinners)
                
            return jsonableArray
    
    def setAlacarteMenu(self, allMealsInFile):
        self._connect()
        AlacarteBridge.lastImportedAlacarteMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO cafeteria.alacarte_menu (tr_type, en_type, start_date, end_date, tr_name, en_name, calorie, protein, food_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (eachMeal['tr_type'], eachMeal['en_type'], eachMeal['startTime'], eachMeal['endTime'], eachMeal['tr_name'], eachMeal['en_name'], eachMeal['calorie'], eachMeal['protein'], eachMeal['food_type']))

                self.connection.commit()
    
