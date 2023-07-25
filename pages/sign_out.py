import time

from pages.base_page import BasePage

class SignOut(BasePage):

    login_button_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[text() = 'Sign in']"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    dashboard_expected_title = "Scouts Panel"
    sign_out_button_xpath = "//span[text() = 'Sign out']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en/login"
    expected_title = "Scouts panel - sign in"
    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.login_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.dashboard_expected_title

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)
        #assert self.get_page_title(self.dashboard_url) == self.expected_title
        assert self.get_page_title(self.login_url) == self.expected_title
