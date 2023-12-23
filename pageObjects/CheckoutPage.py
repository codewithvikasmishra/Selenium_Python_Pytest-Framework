from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage
# from utilities.BaseClass import BaseClass


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.XPATH,"//div[@class='card h-100']")
    productName = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    cardFooter = (By.XPATH,"//div[@class='card h-100']/div/button")
    checkoutProduct = (By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
        # driver.find_element(By.XPATH,"//a[contains(@href,'shop')]") same as above which we used in test_e2e.py
    
    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)
    
    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.productName)
    
    def getProductCheckout(self):
        self.driver.find_element(*CheckOutPage.checkoutProduct).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
    