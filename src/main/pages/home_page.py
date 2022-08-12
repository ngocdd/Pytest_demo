from src.main.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    page_elements = {
        "elements": (By.XPATH, "//h5[.='Elements']"),


    }
