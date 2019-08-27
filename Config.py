from Helpers.DbCredentials import DbCredentials
from os import path


class Config:
    serverType = "Deployment"
    home = path.dirname(__file__)
    dynamicFilesFolderPath = path.join(home, 'dynamicFiles')
    if serverType == 'Test':
        os = 'Windows'
        debug = True
        serverIp = "127.0.0.1"

        staticFolderPath = path.join(home, "imageUploads")
        dynamicFolderPath = path.join(home, "dynamicImages")
        loggerPath = path.join(home, 'log.txt')
        cafeteriaMenuExcelPath = path.join(home, 'Cafeteria', 'cafeteriaMenu.xlsx')
        alacarteMenuExcelPath = path.join(home, 'Alacarte', 'alacarteMenu.xlsx')

    else:
        os = 'Linux'
        debug = False
        serverIp = "144.122.156.67"

        staticFolderPath = "/home/ncc-mobileapp/metumobile2/imageUploads/"
        dynamicFolderPath = "/home/ncc-mobileapp/metumobile2/dynamicImages/"
        loggerPath = 'log.txt'
        cafeteriaMenuExcelPath = '/home/ncc-mobileapp/metumobile2/Cafeteria/cafeteriaMenu.xlsx'
        alacarteMenuExcelPath = '/home/ncc-mobileapp/metumobile2/Alacarte/alacarteMenu.xlsx'

    serverPort = 1072
    serverRootLink = "http://" + serverIp + ":" + str(serverPort)
    cafeteriaMenuServiceUrl = "http://144.122.156.67:1072/cafeteriamenu/"
    alacarteMenuServiceUrl = "http://144.122.156.67:1072/alacartemenu/"
    announcementServiceUrl = "http://144.122.156.67:1072/announcements/category"
    shuttleScheduleServiceUrl = "http://144.122.156.67:1072/shuttleschedule/"
    shuttleScheduleServiceUrl2 = "http://144.122.156.67:1072/shuttleschedule2/111"
    phoneBookServiceUrl = "http://144.122.156.67:1072/phonebook/"
    bookletServiceUrl = "http://144.122.156.67:1072/booklets/"
    brochureServiceUrl = "http://144.122.156.67:1072/brochures/"
    eventsServiceUrl = "http://144.122.156.67:1072/upcomingevents/"
    
