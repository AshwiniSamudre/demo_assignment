import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.LoginPage import LoginPage
from TestData.SignUpData import SignUpData
from utils.BaseClase import BaseClass
from PageObject.SignupPage import SignupPage
from selenium.webdriver.support import expected_conditions as EC

class TestSignupPage(BaseClass):

    def test_signup_page(self,getData):

        self.driver.implicitly_wait(10)

        SignUp = SignupPage(self.driver)
        SignUp.getsignup().click()

        # element = EC.presence_of_element_located(SignUp.getUsername())
        # WebDriverWait(self.driver, 15).until( SignUp.getUsername())

        time.sleep(5)
        SignUp.getUsername().clear()

        SignUp.getUsername().send_keys(getData["username"])
        SignUp.getPassword().send_keys(getData["password"])
        SignUp.getSignup_button().click()
        time.sleep(5)
        Alert_win = self.driver.switch_to.alert
        # Alert_win = EC.presence_of_element_located(self.driver.switch_to.alert)
        # WebDriverWait(self.driver, 15).until(Alert_win)
        SignupMessage = Alert_win.text
        assert "successful" in SignupMessage

        Alert_win.accept()
        time.sleep(5)
        # SignUp.getClose_button().click()
        time.sleep(5)


    ###reading data from the home data page keyworddriven (use dictonary for key value pairs)
    @pytest.fixture(params=SignUpData.test_Signup)
    def getData(self, request):
        return request.param


