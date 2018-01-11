# -*- coding: utf-8 -*-

import sys, os
from datetime import datetime
from flask import Flask, jsonify, request, render_template
from Announcements import Announcements
from Booklets import Booklets
from Cafeteria import Cafeteria
from Cafeteria.ExcelImport import ExcelImport
from Cafeteria.Rating import CafeteriaRating
from Config import Config
from Events import Events
from Helpers.SiteMap import SiteMap
from Phonebook import Phonebook
from Shuttle.ShuttleLocation import ShuttleLocation
from Shuttle import Shuttle
from Admin import Admin
from ImageProcessor import ImageProcessor
import hashlib
from Weather import Weather

lastModificationTime = datetime.now()

sys.stdout.flush()
print ("Server is starting...")

app = Flask(__name__)


def cacheVersion():
    # return new cache every time clients ask.
    # md5Hash = hashlib.md5(str(lastModificationTime)).hexdigest()
    md5Hash = hashlib.md5(str(lastModificationTime)+str(datetime.now().date())).hexdigest()
    return jsonify(cacheVersion=md5Hash)

def cacheVersionOf(data):
    change=""
    change=change+str(1)
    
    data = str(data)+str(change)
    md5Hash = hashlib.md5(data).hexdigest()
    return jsonify(cacheVersion=md5Hash)

def readFromWeb(url):
    import urllib
    resource = urllib.urlopen(url)
    return str(resource.read().decode('utf-8'))

# BEG MENU UPLOAD_______
APP_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/services/cafeteria/excelupload")
def index():
    return render_template("upload.html")

@app.route("/services/cafeteria/exceluploadrawpost", methods=['POST'])
def upload():
    target = os.path.join(APP_DIR, "Cafeteria")
    if not os.path.isdir(target):
        os.mkdir(target)

    selected_files = request.files.getlist("file")
    time_stamp = datetime.now().isoformat()
    for file in selected_files:
        file_name = time_stamp+'_'+file.filename
        destination = os.path.join(Config.dynamicFilesFolderPath, file_name)# "/".join([target, file_name])
        file.save(destination)
        ExcelImport(destination).updateCafeteriaMenu()

    return render_template("complete.html")
# _______END MENU UPLOAD

@app.route('/images/<fileName>')#
def getImageProcessorDynamicFile(fileName):
    from flask import send_from_directory
    resolution = str(request.values.get('resolution'))
    fileName = str(fileName)

    if resolution != "None":
        thumbnailFileName = fileName + "." + resolution + ".jpeg"
        response = send_from_directory(Config.dynamicFolderPath, thumbnailFileName)
    else:
        response = send_from_directory(Config.staticFolderPath, fileName)

    return response

@app.route('/services/excelexport/<path:path>')
def excelImportService(path):
    from flask import send_from_directory
    from Admin.ExcelExport import ExcelExport
    from Config import Config
    from Helpers.JsonApi import JsonApi

    export = ExcelExport(jsonUrl= "http://localhost:1072/" + path + "?expandforexcelexport=1", nameOfArrayVariableToListInExcelExportFile=JsonApi().findNameOfTheArrayAtTheTopLevel())
    exportFileName = export.do()

    response = send_from_directory(Config.dynamicFilesFolderPath, exportFileName,
                                   as_attachment=True,
                                   attachment_filename=exportFileName
                                   )

    return response


@app.route('/announcements/category', defaults={'categoryId': -1})
@app.route('/announcements/category/<categoryId>/')
def fetchAnnouncementCategory(categoryId):
    result = Announcements().fetchCategory(int(categoryId))
    return jsonify(result)


@app.route('/announcements/cacheversion/')
def announcementsCache():
    data1 = readFromWeb(Config.announcementServiceUrl + "/0")
    data2 = readFromWeb(Config.announcementServiceUrl + "/1")
    return cacheVersionOf((data1)+(data2))


@app.route("/admincommands/updatecafeteriamenu")
def updateCafeteriaMenu():
    Admin().checkSuperAdminAuth(request.values.get('pw'))
    ExcelImport().updateCafeteriaMenu()
    return "200"

@app.route("/admincommands/processimages")
def processImages():
    Admin().checkSuperAdminAuth(request.values.get('pw'))
    ImageProcessor().processAllStaticPhotos()
    return "200"


@app.route('/cafeteria/rating/<mealId>', methods=['POST'])
def rateCafeteria(mealId):
    return CafeteriaRating().rateMenu(mealId)

@app.route('/cafeteria/rating/<mealId>', methods=['GET'])
def showRating(mealId):
    return jsonify(mealRating=CafeteriaRating().getMealRating(str(mealId)))

@app.route('/ip/')
def whatsTheServerIp():
    return jsonify(serverIp=Config.serverIp)


@app.route('/ip/cacheversion/')
def whatsTheServerIpCache():
    return cacheVersionOf(whatsTheServerIp())


@app.route('/shuttleschedule/')
def shuttleSchedule():
    return jsonify(ShuttleSchedule=Shuttle.getWeeklySchedule())

@app.route('/shuttleschedule2/')
def shuttleSchedule2():
    return jsonify(ShuttleSchedule2=Shuttle.getWeeklySchedule2())


@app.route('/shuttle/location/')
def shuttleLocation():
    return jsonify(ShuttleLocation=ShuttleLocation().fetchAll())


@app.route('/shuttle/location/raw/')
def shuttleLocationRaw():
    Admin().checkSuperAdminAuth(request.values.get('pw'))
    return jsonify(ShuttleLocation=ShuttleLocation().raw())


@app.route('/shuttle/location/multipleshuttles/')
def multipleShuttleLocations():
    return jsonify(MultipleShuttleLocation=ShuttleLocation().multipleshuttles())


@app.route('/shuttleschedule/cacheversion/')
def cacheShuttle():
    return cacheVersionOf(shuttleSchedule())


@app.route('/cafeteriamenu/')
def cafeteriaMenu():
    version = request.values.get('version')
    try:
        version = float(version)
    except:
        version = 1.0
    return jsonify(CafeteriaMenu=Cafeteria().getUpcomingSchedule(version=version))


@app.route('/services/cafeteria/upcomingmeals/')
def cafeteriaUpcomingMeals():
    version = request.values.get('version')
    try:
        version = float(version)
    except:
        version = 1.0
    return jsonify(CafeteriaMenu=Cafeteria().getUpcomingSchedule(version=version))

@app.route('/services/cafeteria/meals/')
@app.route('/services/cafeteria/allmeals/')
def cafeteriaAllMeals():
    return jsonify(CafeteriaMenu=Cafeteria().getAllMeals())

@app.route('/services/cafeteria/meals/<mealId>')
def cafeteriaMeals(mealId):
    from bson import ObjectId
    return jsonify(Cafeteria().getMeal(mealId=ObjectId(mealId)))

@app.route('/cafeteriamenu/cacheversion/')
def cacheCafeteria():
    return cacheVersionOf(Cafeteria().getAllMeals())


@app.route('/services/cafeteriarate/meals/')
def cafeteriaRateMeals():
    try:
        expandforexcelexport = request.values.get('expandforexcelexport') in ['true', '1']
    except:
        expandforexcelexport = False
    mealRatings = CafeteriaRating().getMealRating()
    if expandforexcelexport:
        mealRatings = Cafeteria().expandRatingsWithMeal(mealRatings)
        for mealRating in mealRatings:
            mealRating['numberOfRates'] = CafeteriaRating().getMealRateCount(mealId = mealRating['_id'])
    result = jsonify(mealRatings = mealRatings)
    return result


@app.route('/upcomingevents/')
def upcomingEvents():
    return jsonify(UpcomingEvents=Events().getUpcomingEvents())


@app.route('/upcomingevents/raw/')
def upcomingEventsRaw():
    return jsonify(UpcomingEvents=Events().getRawUpcomingEvents())


@app.route('/upcomingevents/cacheversion/')
def cacheEvents():
    return cacheVersionOf(upcomingEventsRaw())


@app.route('/phonebook/')
def phonebook():
    data = Phonebook().getPhonebookRecords()
    return jsonify(Phonebook=data)


@app.route('/phonebook/raw/')
def phonebookRaw():
    return jsonify(Phonebook=Phonebook().getRawPhonebookRecords())


@app.route('/phonebook/cacheversion/')
def cachePhonebook():
    return cacheVersionOf(phonebook())


@app.route('/academiccalendar/')
def academicCalendar():
    from Announcements.MetuAnnouncementsBridge import MetuAcademicAndDormCalendarBridge
    result = MetuAcademicAndDormCalendarBridge().fetchAcademicAnnouncements()
    return jsonify(AcademicCalendar=result)


@app.route('/academiccalendar/cacheversion/')
def cacheAcademicCalendar():
    return cacheVersionOf(academicCalendar())


@app.route('/booklets/')
def booklets():
    return jsonify(Booklets=Booklets().getBooklets())


@app.route('/booklets/cacheversion/')
def cacheBooklets():
    return cacheVersionOf(booklets())


@app.route('/featuredApps/ios/')
def iosFeaturedApps():
    links = [
        {
        "en_appName": "Radio ODTU Northern Cyprus Studios",
        "tr_appName": "Radyo ODTU Kuzey Kıbrıs Stüdyoları",
        "storeLink": "https://itunes.apple.com/tr/app/radyo-odtu-kks/id1126479317"
        }
    ]
    return jsonify(FeaturedApps=links)

@app.route('/featuredApps/android/')
def androidFeaturedApps():
    links = [
        {
        "en_appName": "Radio ODTU Northern Cyprus Studios",
        "tr_appName": "Radyo ODTU Kuzey Kıbrıs Stüdyoları",
        "storeLink": "https://play.google.com/store/apps/details?id=com.tanss.radyoodtukks"
        }
    ]
    return jsonify(FeaturedApps=links)

@app.route('/featuredApps/windows/')
def windowsFeaturedApps():
    links = [
        {
        "en_appName": "Radio ODTU Northern Cyprus Studios",
        "tr_appName": "Radyo ODTU Kuzey Kıbrıs Stüdyoları",
        "storeLink": "https://www.microsoft.com/en-us/store/p/radyo-odtu-k%C4%B1br%C4%B1s/9nblggh52pwh"
        }
    ]
    return jsonify(FeaturedApps=links)


@app.route('/services/weather/overall')
def getDailyWeather():
    return jsonify(DailyForecast=Weather().getDaily())


@app.route("/")
def rootPage():
    return SiteMap.siteMapString


@app.route("/services/cache/mastercache")
def mastercache():
    return cacheVersionOf(
        str(cacheBooklets()) +
        str(cacheAcademicCalendar()) +
        str(cachePhonebook()) +
        str(cacheEvents()) +
        str(cacheCafeteria()) +
        str(cacheShuttle()) +
        str(whatsTheServerIpCache()) +
        str(announcementsCache())
    )

@app.route('/metu/ncc/cng/')
def test():
    return jsonify(MyTestValue=str(3.14))







if __name__ == "__main__":
    import logging
    handler = logging.FileHandler(Config.loggerPath)  # errors logged to this file
    handler.setLevel(logging.ERROR)  # only log errors and above

    app.logger.addHandler(handler)  # attach the handler to the app's logger

    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.run(debug=Config.debug, host='0.0.0.0', port=1072, threaded=True)
