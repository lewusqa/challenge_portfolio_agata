import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ChooseTheLeg(BasePage):

    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    add_player_xpath = "//*[text()='Add player']"
    submit_button_xpath = "//button[@type='submit']"
    add_a_player_expected_title = "Add player"
    #add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/login"
    dashboard_url = "https://dareit.futbolkolektyw.pl/en"
    add_a_player_url = "https://dareit.futbolkolektyw.pl/en/players/add"
    expected_title = "Scouts panel - sign in"
    right_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    left_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    select_leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    main_page_xpath = "//span[text()='Main page']"
    added_player_expected_title = "Edit player Agata Panek"
    added_player_url = "https://dareit.futbolkolektyw.pl/en/players/64cfc3625fae9831ba6852a2/edit"

    def select_leg(self,leg):
        self.wait_for_element_to_be_clickable(self.select_leg_dropdown_xpath)
        self.click_on_the_element(self.select_leg_dropdown_xpath)
        if leg == "left":
            #self.wait_for_element_to_be_clickable(self.left_leg_xpath)
            #self.click_on_the_element(self.left_leg_xpath)
            left_leg = self.wait_for_element_to_be_clickable(self.left_leg_xpath)
            left_leg.click()
        else:
            #self.click_on_the_element(self.right_leg_xpath)
            right_leg = self.wait_for_element_to_be_clickable(self.right_leg_xpath)
            right_leg.click()

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        check_title = self.get_page_title(self.add_a_player_url)
        print("check title:", check_title)
        print("add_a_player_expected_title", self.add_a_player_expected_title)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert check_title == self.add_a_player_expected_title


    def click_add_player(self):
        self.click_on_the_element(self.add_player_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title

    def click_main_page(self):
        self.click_on_the_element(self.main_page_xpath)

    def check_last_added_player(self, player_name):
        last_created_player_name_xpath = f"//span[@class='MuiButton-label' and contains(text(), '{player_name}')]"
        try:
            player_element = self.wait_for_visibility_of_element_located(last_created_player_name_xpath, By.XPATH)
            print(f"Player '{player_name}' found.")
        except TimeoutException:
            print(f"Player '{player_name}' not found.")
            raise AssertionError(f"Player '{player_name}' not found.")

