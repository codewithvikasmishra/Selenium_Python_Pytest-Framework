from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import time
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")

        products = checkOutPage.getCardTitle()

        for product in products:
            log.info(checkOutPage.getProductName().text)
            if checkOutPage.getProductName().text == "Blackberry":
                checkOutPage.getCardFooter().click()

        confirmPage = checkOutPage.getProductCheckout()
        log.info("Entering country name as ind")

        confirmPage.getCheckoutItem().click()
        confirmPage.getListCountry().send_keys("ind")

        self.verifyLinkPresence("India")

        confirmPage.getCountryName().click()
        confirmPage.getCheckBox().click()
        confirmPage.getSubmit().click()
        success_text = confirmPage.getAlertMessage().text
        log.info("text received from application is "+success_text)

        assert "Success! Thank you!" in success_text