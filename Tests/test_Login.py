import time

import pytest
from PageObject.AddProduct import Addproduct
from TestData.LoginData import LoginData
from utils.BaseClase import BaseClass
from PageObject.LoginPage import LoginPage
from Tests.test_Signup import TestSignupPage
from selenium.webdriver.common.action_chains import ActionChains


class TestloginPage(BaseClass):

    def test_login_page(self, getData):
        self.driver.implicitly_wait(10)
        login = LoginPage(self.driver)
        login.getloginlink().click()
        time.sleep(5)
        login.getusername().send_keys(getData["username"])
        login.getpassword().send_keys(getData["password"])
        time.sleep(5)
        login.getloginbutton().click()
        time.sleep(5)


    ###reading data from the home data page keyworddriven (use dictonary for key value pairs)
    @pytest.fixture(params=LoginData.test_login)
    def getData(self, request):
        return request.param
