from selenium.webdriver.common.by import By
from src.main.pages.base_page import BasePage


class TextBoxPage(BasePage):
    page_elements = {
        # Text Box
        "user name": (By.CSS_SELECTOR, "#userName"),
        "email": (By.CSS_SELECTOR, "#userEmail"),
        "current address": (By.CSS_SELECTOR, "#currentAddress"),
        "permanent address": (By.CSS_SELECTOR, "#permanentAddress"),
        "button submit": (By.CSS_SELECTOR, "#submit"),
        "result": (By.CSS_SELECTOR, "#output"),
        "error email style": (By.CSS_SELECTOR, ".mr-sm-2.field-error"),
    }
