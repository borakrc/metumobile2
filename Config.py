from Helpers.DbCredentials import DbCredentials


class Config:
    serverType = "Deployment"

    if serverType == 'Test':
        os = 'Windows'
        debug = True
        serverIp = "127.0.0.1"
        staticFolderPath = "C:\Users\john\PycharmProjects\metumobile\imageUploads\\"
        dynamicFolderPath = "C:\Users\john\PycharmProjects\metumobile\dynamicImages\\"
        loggerPath = 'C:\Users\john\PycharmProjects\metumobile\log.txt'
        cafeteriaMenuExcelPath = 'C:\Users\john\PycharmProjects\metumobile\Cafeteria\cafeteriaMenu.xlsx'
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
    
