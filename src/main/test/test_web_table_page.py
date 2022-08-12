import pytest
import pandas as pd
from src.main.helper.helper import get_parameter_from_excel
from src.main.helper.helper import get_data_frame_from_excel
from src.main.helper.helper import get_data_from_excel
from src.main.helper.helper import check_string_in_data_frame
from src.main.helper.helper import compare_data_frame


@pytest.mark.webtable
class Test_web_table:

    # @pytest.fixture(scope="function", autouse=True)
    def init(self):
        self.HomePage.click_on_element("elements")
        self.ElementsPage.click_on_element("web table")

    @pytest.mark.parametrize("first_name, last_name, email, age, salary, department",
                             get_parameter_from_excel("web_table"))
    @pytest.mark.webtable01
    def test_add_new_data(self, first_name, last_name, email, age, salary, department):
        self.web_table_page.click_on_element("add button")
        self.web_table_page.input_value("first name", first_name)
        self.web_table_page.input_value("last name", last_name)
        self.web_table_page.input_value("email", email)
        self.web_table_page.input_value("age", age)
        self.web_table_page.input_value("salary", salary)
        self.web_table_page.input_value("department", department)
        self.web_table_page.click_on_element("submit")
        tb = self.web_table_page.get_element_text("table")
        print(first_name)
        assert first_name, last_name in tb

    @pytest.mark.webtable02
    def test_validate_textbox(self):
        self.web_table_page.click_on_element("add button")
        self.web_table_page.click_on_element("submit")
        first_name = self.web_table_page.get_css_value("valid", "border-bottom-color")

    @pytest.mark.webtable03
    def test_auto_search(self):
        # self.web_table_page.input_value("search box", "Legal")
        tb = self.web_table_page.get_element_text("table header")

    @pytest.mark.webtable04
    def test_pagination_page(self):
        test_data = get_data_from_excel("web_table")
        for i in range(len(test_data["no"])):
            self.web_table_page.click_on_element("add button")
            self.web_table_page.input_value("first name", test_data["first name"][i])
            self.web_table_page.input_value("last name", test_data["last name"][i])
            self.web_table_page.input_value("email", test_data["email"][i])
            self.web_table_page.input_value("age", test_data["age"][i])
            self.web_table_page.input_value("salary", test_data["salary"][i])
            self.web_table_page.input_value("department", test_data["department"][i])
            self.web_table_page.click_on_element("submit")
        tol_page = self.web_table_page.get_element_text("total pages")
        curr_page = self.web_table_page.get_element_text("page size")
        jump_page = self.web_table_page.get_element_attribute("jump page", "value")
        # print(tol_page)
        assert int(tol_page) > 1

    @pytest.mark.webtable05
    def test_change_pagination(self):
        test_data = get_data_from_excel("web_table")
        for i in range(len(test_data["no"])):
            self.web_table_page.click_on_element("add button")
            self.web_table_page.input_value("first name", test_data["first name"][i])
            self.web_table_page.input_value("last name", test_data["last name"][i])
            self.web_table_page.input_value("email", test_data["email"][i])
            self.web_table_page.input_value("age", test_data["age"][i])
            self.web_table_page.input_value("salary", test_data["salary"][i])
            self.web_table_page.input_value("department", test_data["department"][i])
            self.web_table_page.click_on_element("submit")
        self.web_table_page.click_on_element("page size")
        self.web_table_page.click_on_element("20 rows")
        # get values
        tol_page = self.web_table_page.get_element_text("total pages")
        curr_page = self.web_table_page.get_element_text("page size")
        jump_page = self.web_table_page.get_element_attribute("jump page", "value")
        # print(tol_page)
        assert int(tol_page) == 2

    @pytest.mark.webtable06
    def test_change_pagination(self):
        test_data = get_data_from_excel("web_table")
        for i in range(len(test_data["no"])):
            self.web_table_page.click_on_element("add button")
            self.web_table_page.input_value("first name", test_data["first name"][i])
            self.web_table_page.input_value("last name", test_data["last name"][i])
            self.web_table_page.input_value("email", test_data["email"][i])
            self.web_table_page.input_value("age", test_data["age"][i])
            self.web_table_page.input_value("salary", test_data["salary"][i])
            self.web_table_page.input_value("department", test_data["department"][i])
            self.web_table_page.click_on_element("submit")
        self.web_table_page.input_value("jump page", "2")
        # self.web_table_page.clear_content("jump page")
        # get values
        tol_page = self.web_table_page.get_element_text("total pages")
        curr_page = self.web_table_page.get_element_text("page size")
        jump_page = self.web_table_page.get_element_attribute("jump page", "value")
        # print(tol_page)
        assert int(jump_page) == 2

    @pytest.mark.webtable07
    def test_default_data(self):
        data = self.web_table_page.get_table_data("table header", "table body")
        # print(data)
        df = pd.DataFrame(data)
        df.drop("Action", inplace=True, axis=1)
        # print(type(df))
        # print(df)
        default_table = get_data_frame_from_excel("default_table")
        default_table.drop("No", inplace=True, axis=1)
        # print(type(default_table))
        # print(default_table)
        assert df.equals(default_table)

    @pytest.mark.webtable08
    def test_order_by_ascending_first_name(self):
        # get default data from web table
        df_before = pd.DataFrame(self.web_table_page.get_table_data("table header", "table body"))

        # delete empty column "Action" and index
        df_before.drop("Action", axis=1, inplace=True)
        # df_before.drop(index=0, axis=1, inplace=True)

        # click order first name
        self.web_table_page.click_on_element("first name column")

        # get table data after sort by First Name from website
        df_after = pd.DataFrame(self.web_table_page.get_table_data("table header", "table body"))
        # df_after.drop(index=0, axis=1, inplace=True)
        df_after.drop("Action", axis=1, inplace=True)

        # use pandas to sort First Name column by ascending
        df_before.sort_values(ascending=True, by="First Name", inplace=True)

        print(df_before)
        print(df_after)
        assert compare_data_frame(df_before, df_after)

    @pytest.mark.webtable09
    def test_order_by_ascending_last_name(self):
        # get default data from web table
        df_before = pd.DataFrame(self.web_table_page.get_table_data("table header", "table body"))

        # delete empty column "Action" and index
        df_before.drop("Action", axis=1, inplace=True)
        # df_before.drop(index=0, axis=1, inplace=True)

        # click order first name
        self.web_table_page.click_on_element("last name column")

        # get table data after sort by First Name from website
        df_after = pd.DataFrame(self.web_table_page.get_table_data("table header", "table body"))
        # df_after.drop(index=0, axis=1, inplace=True)
        df_after.drop("Action", axis=1, inplace=True)

        # use pandas to sort First Name column by ascending
        df_before.sort_values(ascending=True, by="Last Name", inplace=True)

        print(df_before)
        print(df_after)

    @pytest.mark.webtable10
    @pytest.mark.parametrize("keyword", get_parameter_from_excel("search_box"))
    def test_search_function_valid_keyword(self, keyword):
        # print(keyword)

        # type search keyword
        self.web_table_page.input_value("search box", keyword)

        # get search result
        tb_data = pd.DataFrame(self.web_table_page.get_table_data("table header", "table body"))

        check = check_string_in_data_frame(*keyword, tb_data, "column")

        # assert
        # print(f"table data: \n {tb_data}")
        # print(f"check result \n {check}")
        assert check is True

    @pytest.mark.webtable11
    def test_delete_table_item(self):
        # set item want to delete
        self.web_table_page.temp_locator = "kierra@example.com"
        print(self.web_table_page.temp_locator)
        self.web_table_page.input_value("delete","aaa")

    @pytest.mark.tc12
    def test_nopcommerce(self):
        self.web_table_page.input_value("email", "admin@yourstore.com")
        self.web_table_page.input_value("password", "admin")
        self.web_table_page.click_on_element("submit")

