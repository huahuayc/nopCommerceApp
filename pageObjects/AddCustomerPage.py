import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer Page
    linkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLasName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompany_xpath = "//input[@id='Company']"

    txtcustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"  #?
    lstitemAdministrator_xpath ="//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuest_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpmgrofVendors_xpath="//select[@id='VendorId']"

    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrator_xpath)
        elif role == "Guests":
            # here user can be Registered ( or) Guest, only one
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuest_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerofVender(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrofVendors_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLasName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, comyname):
        self.driver.find_element(By.XPATH, self.txtCompany_xpath).send_keys(comyname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()













