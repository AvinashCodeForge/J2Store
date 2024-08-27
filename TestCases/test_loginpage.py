import pytest

from PageObject.LoginPage import LoginPage
from Utilities.customLogger import LogGen
import configparser


class Test_001_login:

    config = configparser.ConfigParser()
    config.read("..\\Configuration\\config.ini")

    baseurl = 'http://j2store.net/v3/administrator/index.php'
    username = 'manager'
    password = 'manager'

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("********* Test_001_Case *********")
        self.logger.info("********* Verifying Home Page Title *********")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == 'J2Store PRO admin Demo - Administration':
            assert True
            self.driver.close()
            self.logger.info("********* Home Page Title is Passed *********")
        else:
            self.driver.save_screenshot(filename=".\\Screenshots\\" + "logintitle.png")
            self.driver.close()
            self.logger.info("********* Home Page Title is Failed *********")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.credentials('Username', self.username)
        self.lp.credentials('Password', self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Control Panel - J2Store PRO admin Demo - Administration':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(filename=".\\Screenshots\\" + "AfterLoginTitle.png")
            self.driver.close()
            assert False
