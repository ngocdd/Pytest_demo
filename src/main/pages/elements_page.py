from selenium.webdriver.common.by import By
from src.main.pages.base_page import BasePage


class ElementsPage(BasePage):

    page_elements = {
        "text box": (By.XPATH, "//span[text()='Text Box']"),
        "check box": (By.XPATH, "//span[text()='Check Box']"),
        "radio button": (By.XPATH, "//span[text()='Radio Button']"),
        "web table": (By.XPATH, "//span[text()='Web Tables']"),
        "button": (By.XPATH, "//span[text()='Buttons']"),
        "links": (By.XPATH, "//span[text()='Links']")

    }

