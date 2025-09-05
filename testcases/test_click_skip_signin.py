from pageobjects.HomePage import HomePage
from pageobjects.Registration import Registration
import os

from utilities import randomstring
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestSkipSignIn:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging
    #baseURL = "https://demo.automationtesting.in/Index.html"
    def test_click_skip_signin(self,setup):

        self.logger.info('*** SKIP SIGNIN STARTED ****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp= HomePage(self.driver)
        self.hp.click_skipsignin()

        self.reg = Registration(self.driver)
        self.reg.set_firstname("Asha")
        self.reg.set_lastname("Ram")
        self.reg.set_email(randomstring.random_string_generator()+"@gmail.com")
        self.reg.set_phone("987654321")
        self.logger.info('Testcase finished')
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "\\Registration.png")
        self.driver.close()



