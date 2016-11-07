from CredentialsConfig import CredentialsConfig


class Admin:
    def checkSuperAdminAuth(self, pwString):
        if pwString == CredentialsConfig.superAdminPassword:
            return True
        else:
            raise Exception