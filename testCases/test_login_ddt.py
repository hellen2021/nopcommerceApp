import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.get_application_url()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_DDT_Login *******************")
        self.logger.info("************** Verifying login DDT Test *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in an Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            # Log the retrieved values
            self.logger.info(f"Row {r} - Username: {self.user}, Password: {self.password}")

            # Check for None values
            if self.user is None or self.password is None:
                self.logger.error("Username or password is None")
                lst_status.append("Fail")
                continue  # Skip to the next iteration

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)

            # Ensure the page is fully loaded before clicking the login button
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']"))
                )
                login_button = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@value='Log in']"))
                )
                login_button.click()
            except TimeoutException as e:
                self.logger.error(f"Exception occurred while clicking login: {str(e)}")
                self.driver.save_screenshot(f"screenshots/login_error_{r}.png")  # Save screenshot for debugging
                lst_status.append("Fail")
                continue

            # Wait for the page title to indicate successful login
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.title_is("Dashboard / nopCommerce administration")
                )
                act_title = self.driver.title
            except TimeoutException as e:
                act_title = self.driver.title
                self.logger.error(f"Exception occurred while waiting for title: {str(e)}")
                self.driver.save_screenshot(f"screenshots/title_error_{r}.png")  # Save screenshot for debugging

            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************** Passed *******************")
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Test Passed")
                elif self.exp == "Fail":
                    self.logger.info("************** Failed *******************")
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Test Failed")
            else:
                if self.exp == "Pass":
                    self.logger.info("************** Failed *******************")
                    lst_status.append("Fail")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Test Failed")
                elif self.exp == "Fail":
                    self.logger.info("************** Passed *******************")
                    lst_status.append("Pass")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Test Passed")

            # Use explicit wait for the logout button to be clickable and then click it
            try:
                logout_button = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
                )
                logout_button.click()
            except TimeoutException as e:
                self.logger.error(f"Exception during logout: {str(e)}")
                self.driver.save_screenshot(f"screenshots/logout_error_{r}.png")  # Save screenshot for debugging
                lst_status.append("Fail")
                break

        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT test Passed ***")
            assert True
        else:
            self.logger.info("*** Login DDT test Failed ***")
            assert False

        self.driver.close()
        self.logger.info("*********** End of Login DDT Test *****************")
        self.logger.info("*********** Completed TC_LoginDDT_002 *******")
