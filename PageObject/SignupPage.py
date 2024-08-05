from selenium.webdriver.common.by import By

class SignupPage:

    def __init__(self, driver):
        self.driver = driver


    signup = (By.LINK_TEXT, "Sign up")
    Username = (By.XPATH,"(//input[@type='text'])[3]")
    password = (By.XPATH,"//input[@id='sign-password']")
    signupButton = (By.XPATH,"//button[text()='Sign up']")
    closeButton = (By.XPATH,"//button[text()='Close']")


    def getsignup(self):
        return self.driver.find_element(*SignupPage.signup)

    def getUsername(self):
        return self.driver.find_element(*SignupPage.Username)

    def getPassword(self):
        return self.driver.find_element(*SignupPage.password)

    def getSignup_button(self):
        return self.driver.find_element(*SignupPage.signupButton)

    def getClose_button(self):
        return self.driver.find_element(*SignupPage.closeButton)





