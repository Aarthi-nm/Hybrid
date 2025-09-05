from selenium.webdriver.common.by import By


class DashboardPage():
    #Locators
    drpdown_user_xpath = "//p[@class='//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']']"
    menu_logout_xpath = "//a[normalize-space()='Logout']"

    #constructors
    def __init__(self,driver):
        self.driver = driver

    def Clickdrpdown(self):
        self.driver.find_element(By.XPATH, self.drpdown_user_xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH, self.menu_logout_xpath).click()