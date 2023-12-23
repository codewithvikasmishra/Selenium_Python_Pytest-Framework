from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import time
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()

        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])

        log.info("email is "+getData["email"])

        homepage.getEmail().send_keys(getData["email"])
        homepage.getRadio().click()

        # static Dropdown
        log.info("gender is "+getData["gender"])
        self.selectOptionByText(homepage.getGender(),getData["gender"])

        homepage.getPassword().send_keys("123456")
        homepage.getPasswordButton().click()

        # Create Xpath for any element
        # //tagname[@attribute='value']
        # example - //input[@type='submit']
        homepage.getSubmit().click()
        message = homepage.getAlert().text
        print(message)

        assert "Success! The Form has been submitted successfully!." in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param