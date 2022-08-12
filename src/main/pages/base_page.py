from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.main.helper.helper import get_config
import platform


class BasePage(object):

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.webdriver = kwargs["webdriver"]
        self.keys = kwargs["keys"]
        self.time_out = get_config("explicit_wait")
        self.webdriver_wait = kwargs["webdriver_wait"]
        self.platform = platform.system()  # check platform when sen keys

    def check_element_click_able(self, element):
        # get method and locator from page_elements dictionary
        method = self.page_elements[element][0]
        locator = self.page_elements[element][1]
        # explicit wait
        condition = self.webdriver_wait(self.driver, timeout=self.time_out).until(EC.element_to_be_clickable((method,
                                                                                                              locator)))
        return condition

    def wait_element(self, element):
        # fluent wait
        # get method and locator from page_elements dictionary
        method = self.page_elements[element][0]
        locator = self.page_elements[element][1]
        wait = self.webdriver_wait(self.driver, timeout=self.time_out, poll_frequency=1,
                             ignored_exceptions=[EC.NoAlertPresentException])
        element = wait.until(EC.element_to_be_clickable((method, locator)))
        return element

    def get_total_elements(self, element):
        # use find elements to get all elements have same locator in DOM
        total_elements = self.driver.find_elements(*self.page_elements[element])
        return len(total_elements)

    def click_on_element(self, element, *args):
        element = self.wait_element(element)
        element.click()
        # self.driver.find_element(*self.page_elements[element]).click()

    def input_value(self, element, value):
        # clear text box before input value
        # print(f"input phart: {self.page_elements[element]}")
        element = self.driver.find_element(*self.page_elements[element])
        if self.platform == "Darwin":  # Darwin mean Mac OS
            element.send_keys(Keys.COMMAND, 'a')
        else:
            element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(value)

    def get_element_text(self, element):
        text = self.driver.find_element(*self.page_elements[element]).text
        return text

    def get_element_attribute(self, element, attribute):
        get_element = self.driver.find_element(*self.page_elements[element])
        attr = get_element.get_attribute(attribute)
        return attr

    def check_button_is_selected(self, element):
        element = self.driver.find_element(*self.page_elements[element]).is_selected()
        return element

    def check_button_is_enabled(self, element):
        element = self.driver.find_element(*self.page_elements[element]).is_enabled()
        return element

    def get_css_value(self, element, css_attribute):
        get_element = self.driver.find_element(*self.page_elements[element])
        cssValue = get_element.value_of_css_property(css_attribute)
        return cssValue

    def clear_content(self, element):
        # clear text box before input value
        self.driver.find_element(*self.page_elements[element]).clear()

    def get_list_text_of_elements(self, element):
        # use locator of table cell or header cell to get data of the table, don't use block locator

        # extract locator from "page_elements" dictionary
        hd_method = self.page_elements[element][0]
        hd_xpath = self.page_elements[element][1]

        # print(f"hd_xpath {hd_xpath}, hd_method{hd_method}")

        # get list text values of element
        list_data = []
        object_data = {}
        # run loop to get all values of the header
        for i in range(self.get_total_elements(element)):
            i += 1  # index of element in DOM start from 1
            # change index of xpath to get all text value of header
            text = self.driver.find_element(hd_method, hd_xpath + "[" + str(i) + "]").text
            # create list header
            if text == " ":
                list_data.append(' ')
            else:
                list_data.append(text)
            object_data[text] = []
        return list_data, object_data

    def get_table_data(self, header_element, body_element):
        # get total number of header and body elements
        total_number_of_header = self.get_total_elements(header_element)
        total_number_of_body = self.get_total_elements(body_element)

        # extract locator from "page_elements" dictionary
        body_method = self.page_elements[body_element][0]
        body_xpath = self.page_elements[body_element][1]

        # get list values of the header to create dictionary storage values for each header
        list_header, table_data = self.get_list_text_of_elements(header_element)

        # run loop to get add of table
        count = 0  # create count to get header keys
        for j in range(total_number_of_body):
            j += 1  # index of element in DOM start from 1
            # get cell text values of each cell
            cell_value = self.driver.find_element(body_method, body_xpath + "[" + str(j) + "]").text
            # check count condition to get correctly list header keys
            if count >= total_number_of_header:
                count = 0
            # if empty do not append it to list
            if cell_value == " ":
                pass
            else:
                table_data[list_header[count]].append(cell_value)
            count += 1
        # return a dict
        return table_data
