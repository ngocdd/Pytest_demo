from selenium.webdriver.common.by import By
from src.main.pages.base_page import BasePage


class WebTablePage(BasePage):

    temp_locator = ""

    page_elements = {
        # main UI
        "add button": (By.ID, "addNewRecordButton"),
        "search box": (By.ID, "searchBox"),
        "first name column": (By.XPATH, "//div[text()='First Name' and @class='rt-resizable-header-content']"),
        "last name column": (By.XPATH, "//div[text()='Last Name' and @class='rt-resizable-header-content']"),
        "age column": (By.XPATH, "//div[text()='Age' and @class='rt-resizable-header-content']"),
        "email column": (By.XPATH, "//div[text()='Email' and @class='rt-resizable-header-content']"),
        "salary column": (By.XPATH, "//div[text()='Salary' and @class='rt-resizable-header-content']"),
        "department column": (By.XPATH, "//div[text()='Department' and @class='rt-resizable-header-content']"),
        "action column": (By.XPATH, "//div[text()='Action' and @class='rt-resizable-header-content']"),
        "table": (By.CLASS_NAME, "rt-table"),
        "first name css": (By.CSS_SELECTOR, "input#firstName.form-control.was-validated"),
        "valid": (By.CSS_SELECTOR, ".form-control.is-invalid, .was-validated .form-control:invalid"),
        # "table header": (By.CSS_SELECTOR, ".rt-thead.-header"),
        "total pages": (By.CLASS_NAME, "-totalPages"),
        "jump page": (By.XPATH, "//input[@type='number']"),
        "page size": (By.CLASS_NAME, "-pageSizeOptions"),
        "5 rows": (By.XPATH, "//option[text()='5 rows']"),
        "10 rows": (By.XPATH, "//option[text()='10 rows']"),
        "20 rows": (By.XPATH, "//option[text()='20 rows']"),
        "25 rows": (By.XPATH, "//option[text()='25 rows']"),
        "100 rows": (By.XPATH, "//option[text()='100 rows']"),
        "table header": (By.XPATH, "//div[starts-with(@class,'rt-thead')]/descendant::div[starts-with(@class,"
                                   "'rt-th rt-resizable-header')]"),
        "table body": (By.XPATH, "//div[@class='rt-tbody']/descendant::div[@class='rt-td' and @role='gridcell']"),

        # pop-up
        "first name": (By.ID, "firstName"),
        "last name": (By.ID, "lastName"),
        "email": (By.ID, "userEmail"),
        "age": (By.ID, "age"),
        "salary": (By.ID, "salary"),
        "department": (By.ID, "department"),
        "submit": (By.ID, "submit"),
        "close button": (By.CLASS_NAME, "close"),

        # icon inside the table
        "edit": (By.XPATH, f"//div[text()='{temp_locator}']/following::div[@class='action-buttons']/child::span[@title='Edit']"),
        "delete": (By.XPATH, f"//div[text()='{temp_locator}']/following::div[@class='action-buttons']/child::span[@title='Delete']"),

        # demo nopcommerce

         "email": (By.CLASS_NAME, "email"),
         "password": (By.CLASS_NAME, "password"),
         "submit": (By.CLASS_NAME, "button-1"),
    }

