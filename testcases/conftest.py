import os
import pytest
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print('Launching Edge Browser....')
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print('Launching Firefox Browser...')
        return driver
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return driver

def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #This will return browser value to the setup method
    return request.config.getoption("--browser")

#########Pytest HTML Report###########
# #This hook is to add Environment info to the HTML report
# def pytest_configure(config):
#     config._metadata['Project Name']='Orange HRM'
#     config._metadata['Tester Name']='Aarthi P'
#
#
# #This hook is to delete/modify Environment info in HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Plugins",None)

#Specifying report folder location and save report timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d%m%Y-%H%M%S")+".html"