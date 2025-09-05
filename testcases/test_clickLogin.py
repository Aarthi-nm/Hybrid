import time

from pageobjects.HomePage import HomePage
from utilities import ExcelUtilities
from pageobjects.Registration import Registration
import os
from pageobjects.DashboardPage import DashboardPage

from utilities import randomstring
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestClickLogin:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    path = os.path.abspath(os.curdir) + '\\testdata\\LoginData.xlsx'
    #baseURL = "https://demo.automationtesting.in/Index.html"
    def test_click_login(self,setup):

        self.logger.info('*** SKIP SIGNIN STARTED ****')
        self.rows = ExcelUtilities.getRowCount(self.path, 'Sheet1')
        lst_status = []
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp= HomePage(self.driver)
        self.dp = DashboardPage(self.driver)

        for r in range(2,self.rows+1):
            self.uname = ExcelUtilities.readData(self.path,'Sheet1',r,1)
            self.pwd = ExcelUtilities.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtilities.readData(self.path, 'Sheet1', r, 3)
            self.hp.setUsername(self.uname)
            self.hp.setPassword(self.pwd)
            self.hp.clickLogin()
            self.targetpage = self.hp.isdashboardpageexists()
            time.sleep(3)

            if self.exp == 'Valid':
                if self.targetpage == True:
                    lst_status.append('Pass')
                    self.dp.Clickdrpdown()
                    self.dp.ClickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp == 'Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.dp.Clickdrpdown()
                    self.dp.ClickLogout()
                else:
                    lst_status.append('Pass')
                    self.dp.Clickdrpdown()
                    self.dp.ClickLogout()
        self.driver.close()

        #Final Validation
        if 'Fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("****End of Data Driven testing****")



