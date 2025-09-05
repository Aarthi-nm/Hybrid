import os

from selenium.webdriver.common.by import By


class Registration:
    #Locators
    txt_firstname_xpath = "//input[@placeholder='First Name']"
    txt_lastname_xpath = "//input[@placeholder='Last Name']"
    txt_email_xpath = "//input[@type='email']"
    txt_phone_xpath = "//input[@type='tel']"
    radio_male_xpath = "//label[normalize-space()='Male']"
    radio_female_xpath = "//label[normalize-space()='FeMale']"

    #constructors
    def __init__(self,driver):
        self.driver = driver

    #actionmethods
    def set_firstname(self,fname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(fname)

    def set_lastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lname)

    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def set_phone(self,phone):
        self.driver.find_element(By.XPATH,self.txt_phone_xpath).send_keys(phone)

    def select_gender(self,gender):
        if gender == 'Male:':
            self.driver.find_element(By.XPATH,self.radio_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH,self.radio_female_xpath).click()



