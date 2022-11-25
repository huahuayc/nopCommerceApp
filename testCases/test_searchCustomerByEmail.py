import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("****Test_004_SearchCustomerbyEamil ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login successfull*****")

        self.logger.info("*** Starting search Customer by email Test ***")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOnCustomerMenuItem()
        time.sleep(3)

        self.searchcust = SearchCustomer(self.driver)
        emailAdd = "victoria_victoria@nopCommerce.com"
        self.searchcust.setEmail(emailAdd)
        self.searchcust.clickSearch()

        time.sleep(5)
        status = self.searchcust.searchCustomerByEmail(emailAdd)
        assert True == status
        self.logger.info(("***Test_004_SearchCustomerbyEamil finished "))
        self.driver.close()




