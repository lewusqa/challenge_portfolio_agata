import time

from pages.base_page import BasePage

class ChooseTheLeg(BasePage):

    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    add_player_xpath = "//*[text()='Add player']"
    submit_button_xpath = "//button[@type='submit']"
    add_a_player_expected_title = "Add player"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/login"
    expected_title = "Scouts panel - sign in"
    right_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    left_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    select_leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    def select_leg(self,leg):
        self.wait_for_element_to_be_clickable(self.select_leg_dropdown_xpath)
        self.click_on_the_element(self.select_leg_dropdown_xpath)
        if leg == "left":
            self.wait_for_element_to_be_clickable(self.left_leg_xpath)
            self.click_on_the_element(self.left_leg_xpath)
        else:
            self.click_on_the_element(self.right_leg_xpath)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.login_field_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player(self):
        self.click_on_the_element(self.add_player_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title