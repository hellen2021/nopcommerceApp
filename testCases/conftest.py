import pytest
from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser............")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser...........")
    elif browser == 'ie':
        driver = webdriver.Ie()
        print("Launching Internet explorer...........")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    return driver


def pytest_addoption(parser):  # this will get the value from CLI/hooks
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome, firefox or ie")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")

############  Pytest HTML Report ######################
# Hook for adding environment info into the HTML Report
'''
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Hellen'
'''

# hook  for delete/modify environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA HOME', None)
    metadata.pop('Plugins', None)

