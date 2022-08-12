import os

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.chrome.options import Options
# element pages
from src.main.pages.elements_page import ElementsPage
from src.main.pages.radio_button_page import RadioButtonPage
from src.main.pages.home_page import HomePage
from src.main.pages.web_table_page import WebTablePage
from src.main.pages.check_box_page import CheckboxPage
# import helper
from src.main.helper.helper import get_config
import time

# global variable
# Chrome Extensions
chrome_extensions = {
    "adblock": "path to extension"
}

driver = None

@pytest.fixture(scope='class', autouse=True)
def init_driver(request, browser):
    global driver

    # list supported browser
    supported_browser = ["chrome", "firefox"]

    # check browser parameter
    if not browser:
        raise Exception('please add --browser argument when run test')
    if browser not in supported_browser:
        raise Exception(f"browser: {browser} is not supported" + f"\n System only supported {supported_browser}")

    # add browser options
    # chOptions = webdriver.ChromeOptions()
    # # chOptions.add_extension(chrome_extensions["adblock"])
    # options = Options()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # install and run Chrome
    if browser == "chrome":
        print("chrome is running...")
        driver = webdriver.Chrome(service=(ChromeService(ChromeDriverManager().install())))
    # install and run Firefox
    if browser in supported_browser and browser == "firefox":
        print("firefox is running...")
        driver = webdriver.Firefox(service=(FirefoxService(GeckoDriverManager().install())))

    # add implicit wait for driver follow value from config.json
    driver.implicitly_wait(get_config("implicitly_wait"))
    driver.set_window_size(1920, 1080)
    # add class parameters

    request.cls.driver = driver
    request.cls.webdriver = webdriver
    request.cls.keys = Keys
    request.cls.webdriver_wait = WebDriverWait

    # init test pages
    request.cls.web_table_page = WebTablePage(driver=request.cls.driver, webdriver=request.cls.webdriver,
                                            keys=Keys, webdriver_wait=request.cls.webdriver_wait)
    request.cls.element_page = ElementsPage(driver=request.cls.driver, webdriver=request.cls.webdriver,
                                            keys=Keys, webdriver_wait=request.cls.webdriver_wait)
    request.cls.radiobutton_page = RadioButtonPage(driver=request.cls.driver, webdriver=request.cls.webdriver,
                                                  keys=Keys, webdriver_wait=request.cls.webdriver_wait)
    request.cls.home_page = HomePage(driver=request.cls.driver, webdriver=request.cls.webdriver,
                                    keys=Keys, webdriver_wait=request.cls.webdriver_wait)
    request.cls.checkbox_page = CheckboxPage(driver=request.cls.driver, webdriver=request.cls.webdriver,
                                            keys=Keys, webdriver_wait=request.cls.webdriver_wait)

    # quit browser after each class
    yield
    time.sleep(3)
    driver.quit()


# add option when run pytest via cli
def pytest_addoption(parser):
    # add --browser option for command line
    parser.addoption("--browser")


# create browser option
@pytest.fixture(scope='class')
def browser(request):
    # get option and return to request when run test function
    return request.config.getoption("--browser")


# auto read base url from config file and run this function before and after each function
@pytest.fixture(scope="function", autouse=True)
def go_to_home_page(request):
    request.cls.driver.get(get_config("base_url"))
    yield
    # request.cls.driver.get(get_config("base_url"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url(get_config("base_url")))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # add directory
            report_directory = os.path.dirname(os.path.abspath(__file__)) + "\\images\\"
            # get test name
            file_name = report.nodeid.split("::")[-1]
            # take screenshot
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file + ".png")
            # add image to html
            extra.append(pytest_html.extras.image(destination_file + ".png"))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = get_config("report title")