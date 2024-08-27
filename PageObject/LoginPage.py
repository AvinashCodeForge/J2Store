from selenium.webdriver.common.by import By


class LoginPage:

    login_btn_xpath = "//button[@tabindex = '5']"
    dropdown_toggle = "//a[text() = 'Content']"
    logout_btn = "Logout"

    def __init__(self, driver):
        self.driver = driver

    # Used Dynamic locator for username and password
    def credentials(self, field_name, value):
        locator = f"//input[contains(@placeholder, '{field_name}')]"
        self.driver.find_element(By.XPATH, locator).clear()
        self.driver.find_element(By.XPATH, locator).send_keys(value)

    # Used xpath locator for interacting with the login button
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    # Used link text locator for interacting with the logout button
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_btn).click()
