from selenium.webdriver.common.by import By
from src.main.pages.base_page import BasePage

class RadioButtonPage(BasePage):

    page_elements = {
        # radio button page
        "yes check": (By.CSS_SELECTOR, "input[id='yesRadio']"),
        "yes button": (By.XPATH, "//input[@id='yesRadio']//parent::div"),
        "impressive button": (By.XPATH, "//input[@id='impressiveRadio']//parent::div"),
        "impressive check": (By.XPATH, "//input[@id='impressiveRadio']"),
        "no button": (By.CSS_SELECTOR, "input[id='noRadio']")
    }