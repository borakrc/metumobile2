from Helpers.DbCredentials import DbCredentials
from os import path


class Config:
    serverType = "Deployment"
    home = path.dirname(__file__)
    if serverType == 'Test':
        os = 'Windows'
        debug = True
        serverIp = "127.0.0.1"
        staticFolderPath = path.join(home, "imageUploads")
        dynamicFolderPath = path.join(home, "dynamicImages")
        loggerPath = path.join(home, 'log.txt')
        cafeteriaMenuExcelPath = path.join(
                home, 'Cafeteria', 'cafeteriaMenu.xlsx'
        )
    else:
        os = 'Linux'
        debug = True
        serverIp = "144.122.156.67"
        staticFolderPath = "/home/ncc-mobileapp/metumobile2/imageUploads/"
        dynamicFolderPath = "/home/ncc-mobileapp/metumobile2/dynamicImages/"
        loggerPath = 'log.txt'
        cafeteriaMenuExcelPath = '/home/ncc-mobileapp/metumobile2/Cafeteria/cafeteriaMenu.xlsx'

    serverPort = 1072
    serverRootLink = "http://" + serverIp + ":" + str(serverPort)
