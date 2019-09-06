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
            sql = "select distinct end_date from alacarte_menu where end_date > NOW() order by end_date asc"
           
            cursor.execute(sql)
            
            self.connection.commit()
            all_dates = cursor.fetchall()
            
            jsonableArray = []
            for each_date in all_dates:

                sql = "select * from alacarte_menu where end_date = '" + each_date['end_date'] + "' and en_type='Lunch' order by end_date asc"
                
                cursor.execute(sql)

                self.connection.commit()
                all_lunch = cursor.fetchall()
                lunches={}
                lunches['soup']={}
                lunches['main1']={}
                lunches['main2']={}
                lunches['vegeterian']={}
                lunches['sider1']={}
                lunches['sider2']={}
                lunches['sider3']={}
                lunches['extra']={}
                for each_lunch in all_lunch:
                    
                    text_file = open("console.txt", "w")
                    text_file.write("food_type: %s\n" % each_lunch['food_type'])
                    text_file.write("tr_name: %s\n" % each_lunch['tr_name'])
                    text_file.write("en_name: %s\n" % each_lunch['en_name'])
                    text_file.write("calorie: %s\n" % each_lunch['calorie'])
                    text_file.write("protein: %s\n" % each_lunch['protein'])
                    text_file.close()
                    
                    if each_lunch['food_type'] == 'soup':
                        lunches['soup']['tr_name']=each_lunch['tr_name']
                        lunches['soup']['en_name']=each_lunch['en_name']
                        lunches['soup']['calorie']=each_lunch['calorie']
                        lunches['soup']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'main1': 
                        lunches['main1']['tr_name']=each_lunch['tr_name']
                        lunches['main1']['en_name']=each_lunch['en_name']
                        lunches['main1']['calorie']=each_lunch['calorie']
                        lunches['main1']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'main2':
                        lunches['main2']['tr_name']=each_lunch['tr_name']
                        lunches['main2']['en_name']=each_lunch['en_name']
                        lunches['main2']['calorie']=each_lunch['calorie']
                        lunches['main2']['protein']=each_lunch['protein'] 
                    elif each_lunch['food_type'] == 'vegeterian':
                        lunches['vegeterian']['tr_name']=each_lunch['tr_name']
                        lunches['vegeterian']['en_name']=each_lunch['en_name']
                        lunches['vegeterian']['calorie']=each_lunch['calorie']
                        lunches['vegeterian']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider1':
                        lunches['sider1']['tr_name']=each_lunch['tr_name']
                        lunches['sider1']['en_name']=each_lunch['en_name']
                        lunches['sider1']['calorie']=each_lunch['calorie']
                        lunches['sider1']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider2':
                        lunches['sider2']['tr_name']=each_lunch['tr_name']
                        lunches['sider2']['en_name']=each_lunch['en_name']
                        lunches['sider2']['calorie']=each_lunch['calorie']
                        lunches['sider2']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'sider3':
                        lunches['sider3']['tr_name']=each_lunch['tr_name']
                        lunches['sider3']['en_name']=each_lunch['en_name']
                        lunches['sider3']['calorie']=each_lunch['calorie']
                        lunches['sider3']['protein']=each_lunch['protein']
                    elif each_lunch['food_type'] == 'extra':
                        lunches['extra']['tr_name']=each_lunch['tr_name']
                        lunches['extra']['en_name']=each_lunch['en_name']
                        lunches['extra']['calorie']=each_lunch['calorie']
                        lunches['extra']['protein']=each_lunch['protein']
                        
                    
                jsonableArray.append(lunches)
            return jsonableArray
    
    def setAlacarteMenu(self, allMealsInFile):
        self._connect()
        AlacarteBridge.lastImportedAlacarteMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO cafeteria.alacarte_menu (tr_type, en_type, start_date, end_date, tr_name, en_name, calorie, protein, food_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (eachMeal['tr_type'], eachMeal['en_type'], eachMeal['startTime'], eachMeal['endTime'], eachMeal['tr_name'], eachMeal['en_name'], eachMeal['calorie'], eachMeal['protein'], eachMeal['food_type']))

                self.connection.commit()
    
