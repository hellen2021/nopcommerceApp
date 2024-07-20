import time

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.get_application_url()
    userEmail = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*********** Test_004_SearchCustomerByEmail_004 *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userEmail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successful **********")

        self.logger.info("********* Start Search customer test *********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("***** Searching customer by FirstName **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Anuj")
        searchcust.setLastName("Singh")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Anuj Singh")
        assert True == status
        self.logger.info("********* TC_SearchCustomerByFirstName_005 Finished ********")

