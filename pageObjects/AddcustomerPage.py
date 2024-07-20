import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.customLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    # add cutomer page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "// input[ @ id = 'FirstName']"
    txtLastName_xpath = "// input[ @ id = 'LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_xpath = "Gender_Female"
    txtDob_xpath = "// input[ @ id = 'DateOfBirth']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[@title='Administrators']"
    lstitemRegistered_xpath = "//li[@title='Registered']"
    lstitemRegisteredClicked_xpath = "//li[@title='Registered']//span[@role='presentation']\
                                        [normalize-space()='×']"
    lstitemGuestClicked_xpath = "//li[@title='Guests']//span[@role='presentation']\
                                        [normalize-space()='×']"
    lstitemGuest_xpath = "//li[@title='Guests']"
    lstitemVendors_xpath = "//li[@title='Vendors']"
    drpmgrOfVendors_xpath = "//select[@id='VendorId']"
    checkboxActive_xpath = "//input[@id='Active']"
    txtCompanyName_xpath = "//input[@id='Company']"
    is_tax_exempt_checkbox_xpath = "//input[@id='IsTaxExempt']"
    newsletter_dropdown_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        try:
            add_new_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.btnAddnew_xpath))
            )
            add_new_button.click()
        except Exception as e:
            print(f"Error encountered: {e}")
        # self.driver.find_element(By. XPATH, self.btnAddnew_xpath)

    def setEmail(self, email):
        try:
            # Wait for the email input field to be present
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txtEmail_xpath))
            )
            email_field.send_keys(email)
        except Exception as e:
            print(f"Error encountered: {e}")
        # self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys()

    def setPassword(self, password):
        try:
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txtPassword_xpath))
            )
            password_field.clear()
            password_field.send_keys(password)
        except Exception as e:
            print(f"Error encountered: {e}")
        # self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        try:
            # Open the Customer Roles dropdown
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.txtcustomerRoles_xpath))
            ).click()

            # If the role is 'Guest', ensure 'Registered' is not selected
            if role == 'Guest':
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, self.lstitemRegisteredClicked_xpath))
                    ).click()
                except Exception as e:
                    print("Registered role was not selected, so no need to deselect.")

                self.listitem = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.lstitemGuest_xpath))
                )

            # If the role is 'Registered', ensure 'Guest' is not selected
            elif role == 'Registered':
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, self.lstitemGuestClicked_xpath))
                    ).click()
                except Exception as e:
                    print("Guest role was not selected, so no need to deselect.")

                self.listitem = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.lstitemRegistered_xpath))
                )

            elif role == 'Administrators':
                self.listitem = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.lstitemAdministrators_xpath))
                )

            elif role == 'Vendors':
                self.listitem = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.lstitemVendors_xpath))
                )

            # Click the selected list item
            self.driver.execute_script("arguments[0].click();", self.listitem)
        except Exception as e:
            print(f"An error occurred: {e}")
    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_xpath)
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        try:
            # Wait for the email input field to be present
            fname_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txtFirstName_xpath))
            )
            fname_field.send_keys(fname)
        except Exception as e:
            print(f"Error encountered: {e}")
        # self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        try:
            # Wait for the email input field to be present
            l_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txtLastName_xpath))
            )
            l_name_field.send_keys(lname)
        except Exception as e:
            print(f"Error encountered: {e}")
        # self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setIsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.is_tax_exempt_checkbox_xpath).click()

    def setNewsletter(self,news):
        self.driver.find_element(By.XPATH, self.newsletter_dropdown_xpath).send_keys(news)

    def setManagerOfVendor(self):
        self.driver.find_element(By.XPATH, self.drpmgrOfVendors_xpath).click()

    def setActive(self):
        try:
            # Wait for the email input field to be present
            active_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.checkboxActive_xpath))
            )
            active_field.click()
        except Exception as e:
            print(f"Error encountered: {e}")
        # self.driver.find_element(By.XPATH, self.checkboxActive_xpath).click()

    def setAdminContent(self, content):
        try:
            # Wait for the email input field to be present
            content_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txtAdminContent_xpath))
            )
            content_field.send_keys(content)
        except Exception as e:
            print(f"Error encountered: {e}")
        # self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
