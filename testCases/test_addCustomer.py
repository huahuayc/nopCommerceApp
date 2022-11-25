import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("****Test_003_AddCustomer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login successfull*****")

        self.logger.info("*** Starting Add Customer Test ***")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOnCustomerMenuItem()
        time.sleep(3)
        self.addCust.clickOnAddnew()


        self.logger.info(" **** Provider customer info ****")
        self.email = random_generator() + "@gmail.com" #email should be unique
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerofVender("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("Hua")
        self.addCust.setLastName("Cooper")
        self.addCust.setDob("7/05/2001")  #format: D/M/YYY
        self.addCust.setCompanyName("Busy bever")
        self.addCust.setAdminContent("This is for testing...")
        self.addCust.clickOnSave()
        self.logger.info(" **** Saving customer info ****")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print("result msg:", self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*** Add customer Test Passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*** Add customer Test Failed ***")
            assert True == False
        self.driver.close()
        self.logger.info("*** Ending Add Customer testing ***")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





