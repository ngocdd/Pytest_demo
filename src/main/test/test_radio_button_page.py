import pytest


@pytest.mark.radio
# @pytest.mark.usefixtures("go_to_home_page")
class TestRadioButtonPage:

    @pytest.fixture(scope="function", autouse=True)
    def init(self):
        self.HomePage.click_on_element("elements")
        self.ElementsPage.click_on_element("radio button")

    @pytest.mark.radio01
    def test_yes_radio_button(self, init):
        self.RadioButtonPage.click_on_element("yes button")
        ele = self.RadioButtonPage.check_button_is_selected("yes check")
        print(ele)
        assert ele

    @pytest.mark.radio02
    def test_impressive_radio_button(self, init):
        self.RadioButtonPage.click_on_element("impressive button")
        ele = self.RadioButtonPage.check_button_is_selected("impressive check")
        print(ele)
        assert ele

    @pytest.mark.radio03
    def test_radio_button_is_enable(self, init):
        ele = self.RadioButtonPage.check_button_is_enabled("no button")
        print(ele)
        assert ele != True


