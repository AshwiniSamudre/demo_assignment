from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    cartlink = (By.LINK_TEXT, "Cart")
    actualProduct = (By.XPATH, "//tbody[@id='tbodyid']//tr//td[2]")
    button_placeOrder = (By.XPATH, "//button[text()='Place Order']")
    name =(By.ID, "name")
    country = (By.ID, "country")
    city=(By.ID, "city")
    cart=(By.ID, "card")
    mounth=(By.ID, "month")
    year =  (By.ID,"year")
    successmsg= (By.XPATH, "//div[@class='sweet-alert  showSweetAlert visible']//h2")
    okButton = (By.XPATH, "//button[text()='OK']")
    def getcartlink(self):
        return self.driver.find_element(*CheckOut.cartlink)

    def getActualproduct(self):
        return self.driver.find_element(*CheckOut.actualProduct)

    def getButton_placeorder(self):
        return self.driver.find_element(*CheckOut.button_placeOrder)

    def getname(self):
        return self.driver.find_element(*CheckOut.name)

    def getcountry(self):
        return self.driver.find_element(*CheckOut.country)
    def getcity(self):
        return self.driver.find_element(*CheckOut.city)

    def getcart(self):
        return self.driver.find_element(*CheckOut.cart)

    def getmonth(self):
        return self.driver.find_element(*CheckOut.mounth)

    def getyear(self):
        return self.driver.find_element(*CheckOut.year)

    def getsuccessmag(self):
        return self.driver.find_element(*CheckOut.successmsg)

    def getOkbutton(self):
        return self.driver.find_element(*CheckOut.okButton)

