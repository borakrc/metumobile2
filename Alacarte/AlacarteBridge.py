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
                lunches['details']={}
                for each_lunch in all_lunch:
                    text_file = open("console.txt", "w")
                    text_file.write("food_type: %s\n" % each_lunch['food_type'])
                    text_file.write("tr_name: %s\n" % each_lunch['tr_name'].encode('utf-8'))
                    text_file.write("en_name: %s\n" % each_lunch['en_name'])
                    text_file.write("calorie: %s\n" % each_lunch['calorie'])
                    text_file.write("protein: %s\n" % each_lunch['protein'])
                    text_file.close()       
                    if each_lunch['food_type'] == 'soup':
                        lunches['details']['soup']={}
                        lunches['details']['soup']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['soup']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['soup']['calorie']=each_lunch['calorie']
                        lunches['details']['soup']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'main1': 
                        lunches['details']['main1']={}
                        lunches['details']['main1']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['main1']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['main1']['calorie']=each_lunch['calorie']
                        lunches['details']['main1']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'main2':
                        lunches['details']['main2']={}
                        lunches['details']['main2']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['main2']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['main2']['calorie']=each_lunch['calorie']
                        lunches['details']['main2']['protein']=each_lunch['protein'] 
                    elif each_lunch['food_type'] == 'vegeterian':
                        lunches['details']['vegeterian']={}
                        lunches['details']['vegeterian']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['vegeterian']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['vegeterian']['calorie']=each_lunch['calorie']
                        lunches['details']['vegeterian']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider1':                        
                        lunches['details']['sider1']={}
                        lunches['details']['sider1']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['sider1']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['sider1']['calorie']=each_lunch['calorie']
                        lunches['details']['sider1']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider2':                        
                        lunches['details']['sider2']={}
                        lunches['details']['sider2']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['sider2']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['sider2']['calorie']=each_lunch['calorie']
                        lunches['details']['sider2']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider3':                        
                        lunches['details']['sider3']={}
                        lunches['details']['sider3']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['sider3']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['sider3']['calorie']=each_lunch['calorie']
                        lunches['details']['sider3']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'extra':                        
                        lunches['details']['extra']={}
                        lunches['details']['extra']['tr_name']=(each_lunch['tr_name']).encode('utf-8')
                        lunches['details']['extra']['en_name']=(each_lunch['en_name']).encode('utf-8')
                        lunches['details']['extra']['calorie']=each_lunch['calorie']
                        lunches['details']['extra']['protein']=each_lunch['protein']
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
                    
                    dinners['details']={}
                    if each_dinner['food_type'] == 'soup':
                        dinners['details']['soup']={}              
                        dinners['details']['soup']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['soup']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['soup']['calorie']=each_dinner['calorie']
                        dinners['details']['soup']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'main1': 
                        dinners['details']['main1']={}
                        dinners['details']['main1']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['main1']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['main1']['calorie']=each_dinner['calorie']
                        dinners['details']['main1']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'main2':
                        dinners['details']['main2']={}
                        dinners['details']['main2']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['main2']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['main2']['calorie']=each_dinner['calorie']
                        dinners['details']['main2']['protein']=each_dinner['protein'] 
                    elif each_dinner['food_type'] == 'vegeterian':
                        dinners['details']['vegeterian']={}
                        dinners['details']['vegeterian']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['vegeterian']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['vegeterian']['calorie']=each_dinner['calorie']
                        dinners['details']['vegeterian']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'sider1':                        
                        dinners['details']['sider1']={}
                        dinners['details']['sider1']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['sider1']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['sider1']['calorie']=each_dinner['calorie']
                        dinners['details']['sider1']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'sider2':                        
                        dinners['details']['sider2']={}
                        dinners['details']['sider2']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['sider2']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['sider2']['calorie']=each_dinner['calorie']
                        dinners['details']['sider2']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'sider3':
                        dinners['details']['sider3']={}
                        dinners['details']['sider3']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['sider3']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['sider3']['calorie']=each_dinner['calorie']
                        dinners['details']['sider3']['protein']=each_dinner['protein']
                    elif each_dinner['food_type'] == 'extra':                        
                        dinners['details']['extra']={}
                        dinners['details']['extra']['tr_name']=(each_dinner['tr_name']).encode('utf-8')
                        dinners['details']['extra']['en_name']=(each_dinner['en_name']).encode('utf-8')
                        dinners['details']['extra']['calorie']=each_dinner['calorie']
                        dinners['details']['extra']['protein']=each_dinner['protein']
                        
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
    
