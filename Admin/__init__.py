from Config import Config

class Admin:
    def checkSuperAdminAuth(self, pwString):
        if pwString == Config.superAdminPassword:
            return True
        else:
            raise Exception