import pytest
from PageObject.LoginPage import LoginPage
from Utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_001_login:
    baseurl = 'http://j2store.net/v3/administrator/index.php'
    username = 'manager'
    password = 'manager'

    logger = LogGen.loggen()

    '''Verifies the home page title.'''
    @pytest.mark.sanity
    def test_homePageTitle(self):
        self.logger.info("********* Test_001_Case *********")
        self.logger.info("********* Verifying Home Page Title *********")
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == 'J2Store PRO admin Demo - Administration':
            assert True
            self.logger.info("********* Home Page Title is Passed *********")
        else:
            self.driver.save_screenshot(filename=".\\Screenshots\\" + "logintitle.png")
            self.logger.info("********* Home Page Title is Failed *********")
            assert False

    '''Verifies the login page title.'''
    @pytest.mark.regression
    def test_login(self):
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.credentials('Username', self.username)
        self.lp.credentials('Password', self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Control Panel - J2Store PRO admin Demo - Administration':
            self.logger.info("********* Home Page Title is Passed *********")
            assert True
        else:
            self.driver.save_screenshot(filename=".\\Screenshots\\" + "AfterLoginTitle.png")
            self.logger.info("********* Home Page Title is Failed *********")
            assert False
