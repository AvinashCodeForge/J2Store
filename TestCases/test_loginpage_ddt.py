import time
from PageObject.LoginPage import LoginPage
from Utilities import ExcelUtils
from Utilities.customLogger import LogGen


class Test_002_login_ddt:
    baseurl = 'http://j2store.net/v3/administrator/index.php'
    file = ".\\TestData\\LoginDataJ2Store.xlsx"

    logger = LogGen.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.file, 'Sheet1')
        print("Number of rows in an Excel", self.rows)

        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.file, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.file, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.file, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = self.driver.title

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append('pass')
                elif self.exp == 'fail':
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append('fail')
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info('** Failed **')
                    lst_status.append('fail')
                elif self.exp == 'fail':
                    self.logger.info('** Passed **')
                    lst_status.append('pass')

        if "fail" not in lst_status:
            self.logger.info("Login DDT is passed.....")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT is failed.....")
            self.driver.close()
            assert False
