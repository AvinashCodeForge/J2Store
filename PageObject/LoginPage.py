from selenium.webdriver.common.by import By


class LoginPage:

    login_btn_xpath = "//button[@tabindex = '5']"
    dropdown_toggle = "//a[text() = 'Content']"
    logout_btn = "Logout"

    def __init__(self, driver):
        self.driver = driver

    # common locator for the username and password
    def credentials(self, field_name, value):
        locator = f"//input[contains(@placeholder, '{field_name}')]"
        self.driver.find_element(By.XPATH, locator).clear()
        self.driver.find_element(By.XPATH, locator).send_keys(value)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.dropdown_toggle).click()
        self.driver.find_element(By.LINK_TEXT, self.logout_btn).click()
