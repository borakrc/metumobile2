from Helpers.DbCredentials import DbCredentials
import os


class Config:
    serverType = "Deployment"
    home = os.path.dirname(__file__)
    if serverType == 'Test':
        os = 'Windows'
        debug = True
        serverIp = "127.0.0.1"
        staticFolderPath = os.path.join(home, "imageUploads")
        dynamicFolderPath = os.path.join(home, "metumobile", "dynamicImages")
        loggerPath = os.path.join(home, 'metumobile', 'log.txt')
        cafeteriaMenuExcelPath = os.path.join(
                home, 'metumobile', 'Cafeteria', 'cafeteriaMenu.xlsx'
        )
    else:
        os = 'Linux'
        debug = False
        serverIp = "144.122.156.67"
        staticFolderPath = "/home/ncc-mobileapp/metumobile/imageUploads/"
        dynamicFolderPath = "/home/ncc-mobileapp/metumobile/dynamicImages/"
        loggerPath = 'log.txt'
        cafeteriaMenuExcelPath = '/home/ncc-mobileapp/metumobile/Cafeteria/cafeteriaMenu.xlsx'

    serverPort = 1072
    serverRootLink = "http://" + serverIp + ":" + str(serverPort)
