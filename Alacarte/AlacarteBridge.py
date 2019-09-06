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
        
        #self.cursor.execute("select * from alacarte_menu where end_date > NOW()")

            jsonableArray = []
            for each_date in all_dates:

                dates = {}
                dates['end_date'] = each_date['end_date']

                sql = "select * from alacarte_menu where end_date =" + each_date['end_date'] + " and en_type='Lunch' order by end_date asc"

                cursor.execute(sql)

                self.connection.commit()
                all_lunch = cursor.fetchall()

                for each_lunch in all_lunch:

                    lunches={}
                    if each_lunch['food_type'] == 'soup':
                        lunches['soup']['tr_name']=each_lunch['tr_name']
                        lunches['soup']['en_name']=each_lunch['en_name']
                        lunches['soup']['calorie']=each_lunch['calorie']
                        lunches['soup']['protein']=each_lunch['protein']
                    if each_lunch['food_type'] == 'main1': 
                        lunches['main1']['tr_name']=each_lunch['tr_name']
                        lunches['main1']['en_name']=each_lunch['en_name']
                        lunches['main1']['calorie']=each_lunch['calorie']
                        lunches['main1']['protein']=each_lunch['protein']
                    if each_lunch['food_type'] == 'main2':
                        lunches['main2']['tr_name']=each_lunch['tr_name']
                        lunches['main2']['en_name']=each_lunch['en_name']
                        lunches['main2']['calorie']=each_lunch['calorie']
                        lunches['main2']['protein']=each_lunch['protein']    
                    
                jsonableArray.append(lunches)  
                    
                
            
            
            
            #meal = {}
            #meal['id'] = str(each['id'])
            #meal['tr_type'] = each['tr_type']
            #meal['en_type'] = each['en_type']
            #meal['start_date'] = each['start_date']
            #meal['end_date'] = each['end_date']
            #meal['tr_name'] = each['tr_name']
            #meal['en_name'] = each['en_name']
            #meal['calorie'] = each['calorie']
            #meal['protein'] = each['protein']
            #meal['food_type'] = each['food_type']
            #jsonableArray.append(meal)

        return jsonableArray
    
    def setAlacarteMenu(self, allMealsInFile):
        self._connect()
        AlacarteBridge.lastImportedAlacarteMenu = allMealsInFile
        for eachMeal in allMealsInFile:
            #assert isinstance(eachMeal, MealContainer)
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO cafeteria.alacarte_menu (tr_type, en_type, start_date, end_date, tr_name, en_name, calorie, protein, food_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (eachMeal['tr_type'], eachMeal['en_type'], eachMeal['startTime'], eachMeal['endTime'], eachMeal['tr_name'], eachMeal['en_name'], eachMeal['calorie'], eachMeal['protein'], eachMeal['food_type']))

                self.connection.commit()
    
