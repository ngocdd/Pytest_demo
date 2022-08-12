from selenium.webdriver.common.by import By
from src.main.pages.base_page import BasePage


class CheckboxPage(BasePage):

    page_elements = {
        # Check Box
        "home toggle": (By.XPATH, "//span[text()='Home']//parent::label//preceding-sibling::button"),
        "home checkbox" : (By.XPATH ,"//span[text()='Home']//preceding-sibling::span[@class='rct-checkbox']"),
        "desktop toggle": (By.XPATH, "//span[text()='Desktop']//ancestor::span//child::button"),
        "desktop checkbox": (By.XPATH, "//span[text()='Desktop']//ancestor::span//child::span[@class='rct-checkbox']"),
        "notes checkbox": (By.XPATH, "//span[text()='Notes']//ancestor::span//child::span[@class='rct-checkbox']"),
        "commands checkbox": (By.XPATH, "//span[text()='Commands']//ancestor::span//child::span[@class='rct-checkbox']"),
        "documents toggle": (By.XPATH, "//span[text()='Documents']//ancestor::span//child::button"),
        "documents checkbox": (By.XPATH, "//span[text()='Documents']//parent::label//child::span[@class='rct-checkbox']"),
        "workspace toggle": (By.XPATH, "//span[text()='WorkSpace']//ancestor::span//child::button"),
        "workspace checkbox": (By.XPATH, "//span[text()='WorkSpace']//parent::label//child::span[@class='rct-checkbox']"),
        "react checkbox": (By.XPATH, "//span[text()='React']//ancestor::span//child::span[@class='rct-checkbox']"),
        "angular checkbox": (By.XPATH, "//span[text()='Angular']//ancestor::span//child::span[@class='rct-checkbox']"),
        "veu checkbox": (By.XPATH, "//span[text()='Veu']//ancestor::span//child::span[@class='rct-checkbox']"),
        "office toggle": (By.XPATH, "//span[text()='Office']//ancestor::span//child::button"),
        "office checkbox": (By.XPATH, "//span[text()='Office']//parent::label//child::span[@class='rct-checkbox']"),
        "public checkbox": (By.XPATH, "//span[text()='Public']//parent::label//preceding-sibling::span[@class='rct-checkbox']"),
        "private checkbox": (By.XPATH, "//span[text()='Private']//parent::label//preceding-sibling::span[@class='rct-checkbox']"),
        "classified checkbox": (By.XPATH, "//span[text()='Classified']//parent::label//preceding-sibling::span[@class='rct-checkbox']"),
        "general checkbox": (By.XPATH, "//span[text()='General']//parent::label//preceding-sibling::span[@class='rct-checkbox']"),
        "downloads toggle": (By.XPATH, "//span[text()='Downloads']//ancestor::span//child::button"),
        "downloads checkbox": (By.XPATH, "//span[text()='Downloads']//parent::label//child::span[@class='rct-checkbox']"),
        "word file checkbox": (By.XPATH, "//span[text()='Word File.doc']//parent::label//preceding-sibling::span[@class='rct-checkbox']"),
        "excel file checkbox": (By.XPATH, "//span[text()='Excel File.doc']//parent::label//preceding-sibling::span[@class='rct-checkbox']"),
        "home checkbox status": (By.XPATH, "//span[text()='Home']//parent::label//*[local-name()='svg' and @class='rct-icon rct-icon-uncheck' or @class='rct-icon rct-icon-check']"),
        "checkbox result": (By.ID, "result"),
        "button expand all": (By.XPATH, "//button[@class='rct-option rct-option-expand-all']"),
        "button collapse all": (By.XPATH, "//button[@class='rct-option rct-option-collapse-all']")

    }