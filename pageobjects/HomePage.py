import pytest
from selenium.webdriver.common.by import By

class HomePage:
    #Locators
    # button_skipsignin_id = "btn2"
    # button_signin_id = "btn1"
    text_username_name = "username"
    text_pwd_name = "password"
    button_login_xpath ="//button[normalize-space()='Login']"
    text_dashboard_xpath = "//h6[normalize-space()='Dashboard']"

    #constructors
    def __init__(self,driver):
        self.driver = driver

    #actionmethods
    # def click_skipsignin(self):
    #     self.driver.find_element(By.ID,self.button_skipsignin_id).click()
    def setUsername(self,uname):
        self.driver.find_element(By.NAME,self.text_username_name).send_keys(uname)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.text_pwd_name).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def isdashboardpageexists(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_dashboard_xpath).is_displayed()
        except:
            return False
