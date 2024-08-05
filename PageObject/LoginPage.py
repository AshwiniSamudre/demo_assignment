from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login = (By.LINK_TEXT,"Log in")
    username = (By.ID,"loginusername")
    password = (By.ID,"loginpassword")
    login_button = (By.XPATH,"//button[text()='Log in']")
    closebutton = (By.XPATH,"(//button[text()='Close'])[3]")

    def getloginlink(self):
        return self.driver.find_element(*LoginPage.login)

    def getusername(self):
        return self.driver.find_element(*LoginPage.username)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getloginbutton(self):
        return self.driver.find_element(*LoginPage.login_button)


