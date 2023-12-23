from selenium.webdriver.common.by import By
# from utilities.BaseClass import BaseClass


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    checkoutItem = (By.XPATH,"//button[@class='btn btn-success']")
    countryName = (By.ID,"country")
    selectCountry = (By.LINK_TEXT,"India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.XPATH,"//input[@type='submit']")
    alert = (By.CLASS_NAME,"alert-success")

    def getCheckoutItem(self):
        return self.driver.find_element(*ConfirmPage.checkoutItem)
    
    def getListCountry(self):
        return self.driver.find_element(*ConfirmPage.countryName)
    
    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)
    
    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    
    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)
    
    def getAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alert)