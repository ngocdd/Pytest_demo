import pytest
from src.main.helper.helper import get_parameter_from_excel


@pytest.mark.tb
@pytest.mark.usefixtures("go_to_home_page")
class TestTextBox:

    @pytest.fixture(scope="function", autouse=True)
    def init(self):
        self.HomePage.click_on_element("elements")
        self.ElementsPage.click_on_element("text box")

    # test happy case
    @pytest.mark.tb01
    @pytest.mark.parametrize("username, email, cur_address, per_address", get_parameter_from_excel("happy_case"))
    def test_valid_input(self, username, email, cur_address, per_address):
        self.element_page.input_values("user name", username)
        self.element_page.input_values("email", email)
        self.element_page.input_values("current address", cur_address)
        self.element_page.input_values("permanent address", per_address)
        self.element_page.click_on_element("button submit")

        # get result
        result = self.element_page.get_element_text("result")
        assert username in result
        assert email in result
        assert cur_address in result
        assert per_address in result

    # test validate email
    @pytest.mark.tb02
    @pytest.mark.parametrize("username, email, cur_address, per_address", get_parameter_from_excel("invalid email"))
    def test_invalid_email(self, username, email, cur_address, per_address):
        self.element_page.input_values("user name", username)
        self.element_page.input_values("email", email)
        self.element_page.input_values("current address", cur_address)
        self.element_page.input_values("permanent address", per_address)
        self.element_page.click_on_element("button submit")

        check = self.element_page.get_element_attribute('error email style', "class")
        assert "field-error" in check
    # test
