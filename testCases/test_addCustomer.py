import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.get_application_url()
    userEmail = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_adddCustomer(self,setup):
        self.logger.info("*********** Test_003_AddCustomer *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userEmail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successful **********")

        self.logger.info("********* Start Add customer test *********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("***** Providing cutomer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("Test@123")
        self.addcust.setFirstName("Hellen")
        self.addcust.setLastName("Cheptoo")
        self.addcust.setGender("Female")
        self.addcust.setDob("03/08/1999")
        self.addcust.setCompanyName("BysyQA")
        self.addcust.setIsTaxExempt()
        self.addcust.setNewsletter("Learn automation testing")
        time.sleep(10)
        self.addcust.setCustomerRoles("Guest")
        self.addcust.setManagerOfVendor()
        self.addcust.setAdminContent("This is for testing .......")
        self.addcust.clickOnSave()

        self.logger.info("***** Saving customer information *****")

        self.logger.info("******* Add customer validation started *****")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("****** Add customer test passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.info("***** Add customer test failed *******")
            assert True == False

def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





