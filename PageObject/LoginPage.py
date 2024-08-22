from selenium.webdriver.common.by import By


class LoginPage:

    text_box_id_username = "mod-login-username"
    text_box_password = "mod-login-password"
    login_btn_xpath = "//button[@tabindex = '5']"
    dropdown_toggle = "//a[text() = 'Content']"
    logout_btn = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.text_box_id_username).clear()
        self.driver.find_element(By.ID, self.text_box_id_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.text_box_password).clear()
        self.driver.find_element(By.ID, self.text_box_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.dropdown_toggle).click()
        self.driver.find_element(By.LINK_TEXT, self.logout_btn).click()



