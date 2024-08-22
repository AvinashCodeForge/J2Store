import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class Readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common Files', 'baseurl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common Files', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common Files', 'password')
        return password
