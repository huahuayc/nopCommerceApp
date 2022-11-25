import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    serv_obj = Service()
    if browser == "chrome":
        driver = webdriver.Chrome(service=serv_obj)
        print("Launching chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox(service=serv_obj)
    elif browser == "edge":
        driver = webdriver.Edge(service=serv_obj)
        print("Launching edge browser")
    else:
        driver = webdriver.Chrome(service=serv_obj)
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")

### PyTest HTML Report ####
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Teseter'] = 'Huahuha'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pyteset_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

