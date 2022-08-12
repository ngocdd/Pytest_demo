import pytest


@pytest.mark.usefixtures("go_to_home_page")
class TestCheckBox:

    @pytest.fixture(scope="function", autouse=True)
    def go_to_checkbox(self):
        self.HomePage.click_on_element("elements")
        self.ElementsPage.click_on_element("check box")

    # test expand home and click on checkbox home
    @pytest.mark.cb01
    def test_check_box(self):
        self.CheckboxPage.click_on_element("home checkbox")
        # self.CheckboxPage.click_on_element("button expand all")
        # self.CheckboxPage.click_on_element("button collapse all")

        result = self.CheckboxPage.get_element_attribute('home checkbox status', "class")
        print(result)
        assert "rct-icon-check" in result
        # self.CheckboxPage.click_on_element("home checkbox")
        # assert "rct-icon-uncheck" in result
