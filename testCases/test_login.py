import pytest

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/login"
    # username = "admin@yourstore.com"
    # password = "admin"
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*****Test_001-Login*****")
        self.logger.info("Verifying Home Page Title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if ( act_title=="Your store. Login123"):
            assert True
            self.driver.close()
            self.logger.info("****Home page title test is passed")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****Home page title test is failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("****Verifying login test ******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**** login test passed ******")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**** login test failed ******")
            assert False


