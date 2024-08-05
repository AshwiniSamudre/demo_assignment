import time

import pytest

from PageObject.checkoutPage import CheckOut
from TestData.ProductData import ProductData
from utils.BaseClase import BaseClass
from PageObject.AddProduct import Addproduct

class TestAddProduct(BaseClass):

    def test_AddProduct(self,getData):

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        addproduct = Addproduct(self.driver)
        addproduct.getHomepage().click()
        time.sleep(5)
        addproduct.getLaptopOption().click()
        time.sleep(5)
        laptops = addproduct.getallLaptops()

        for laptop in laptops:
            print(laptop.text)
            if laptop.text ==getData["laptopName"]:
                laptop.click()

        time.sleep(5)
        # ####checkout page
        selected_Product=addproduct.getselectProduct().text
        print("selected= ",selected_Product)
        assert "MacBook" in selected_Product
        addproduct.getbutoon_AddtoCart().click()
        time.sleep(5)
        alert = self.driver.switch_to.alert
        assert "Product added" in alert.text
        alert.accept()
        cart = CheckOut(self.driver)
        cart.getcartlink().click()
        actual_Product = cart.getActualproduct().text
        print("actualproduct =", actual_Product)
        # selectedproduct = addproduct.getselectProduct().text
        if selected_Product == actual_Product:
            cart.getButton_placeorder().click()
        time.sleep(5)
        cart.getname().send_keys(getData["name"])
        cart.getcountry().send_keys(getData["country"])
        cart.getcity().send_keys(getData["city"])
        cart.getcart().send_keys(getData["cart"])
        cart.getmonth().send_keys(getData["month"])
        cart.getyear().send_keys(getData["year"])
        time.sleep(5)
        # confirmMsg = cart.getsuccessmag().text
        # print(confirmMsg)
        # assert "Thank you for your purchase!" in confirmMsg
        # cart.getOkbutton().click()
        # time.sleep(5)

    @pytest.fixture(params=ProductData.test_addProduct)
    def getData(self, request):
        return request.param