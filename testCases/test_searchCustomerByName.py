import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("****Test_005_SearchCustomerbyName ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login successfull*****")

        self.logger.info("*** Starting search Customer by name Test ***")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOnCustomerMenuItem()
        time.sleep(3)

        self.searchcust = SearchCustomer(self.driver)
        fname = "James"
        lname = "Pan"
        self.searchcust.setFirstName(fname)
        self.searchcust.setLastName(lname)
        self.searchcust.clickSearch()

        time.sleep(5)
        name = "James Pan" #fname + lname
        status = self.searchcust.searchCustomerByName(name)
        assert True == status
        self.logger.info(("***Test_005_SearchCustomerbyName finished "))
        self.driver.close()




