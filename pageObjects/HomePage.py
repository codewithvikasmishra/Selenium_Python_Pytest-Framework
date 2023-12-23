from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage
# from utilities.BaseClass import BaseClass


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH,"//a[contains(@href,'shop')]")
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME,"email")
    radio = (By.CSS_SELECTOR,"#inlineRadio1")
    gender = (By.ID,"exampleFormControlSelect1")
    password = (By.ID,"exampleInputPassword1")
    passwordButton = (By.ID,"exampleCheck1")
    submit = (By.XPATH,"//input[@type='submit']")
    alert = (By.CLASS_NAME,"alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        # driver.find_element(By.XPATH,"//a[contains(@href,'shop')]") same as above which we used in test_e2e.py
    
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    
    def getRadio(self):
        return self.driver.find_element(*HomePage.radio)
    
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    
    def getPasswordButton(self):
        return self.driver.find_element(*HomePage.passwordButton)
    
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    
    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)