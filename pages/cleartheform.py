import time

from pages.base_page import BasePage

class ClearForm(BasePage):

    login_button_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[text() = 'Sign in']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    dashboard_url = "https://dareit.futbolkolektyw.pl/en"
    expected_title = "Scouts Panel"

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_xpath, height)

    def click_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.login_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title