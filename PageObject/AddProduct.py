from selenium.webdriver.common.by import By


class Addproduct:
    def __init__(self, driver):
        self.driver = driver
    home = (By.PARTIAL_LINK_TEXT, "Home")
    laptopOption = (By.LINK_TEXT, "Laptops")
    allLaptops = (By.XPATH, "//div[@id='tbodyid']//h4/a")
    selectProduct= (By.XPATH, "//div[@id='tbodyid']/h2")
    button_Addtocart= (By.LINK_TEXT, "Add to cart")

    def getHomepage(self):
        return self.driver.find_element(*Addproduct.home)

    def getLaptopOption(self):
        return self.driver.find_element(*Addproduct.laptopOption)

    def getallLaptops(self):
        return self.driver.find_elements(*Addproduct.allLaptops)

    def getselectProduct(self):
        return self.driver.find_element(*Addproduct.selectProduct)

    def getbutoon_AddtoCart(self):
        return self.driver.find_element(*Addproduct.button_Addtocart)