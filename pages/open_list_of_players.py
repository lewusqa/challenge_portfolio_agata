import time

from pages.base_page import BasePage

class OpenListOfPlayers(BasePage):

    login_button_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[text() = 'Sign in']"
    players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts Panel"
    #list_of_players_url = "https://scouts-test.futbolkolektyw.pl/en/players"
    dashboard_url = "https://dareit.futbolkolektyw.pl/en"
    list_of_players_url = "https://dareit.futbolkolektyw.pl/en/players"
   #list_players_expected_title = "Players (4309) page 1"  CHANGEABLE!!!

    def click_list_of_players(self):
        self.click_on_the_element(self.players_xpath)
        assert self.get_page_title(self.list_of_players_url) == self.list_players_expected_title
    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.login_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
