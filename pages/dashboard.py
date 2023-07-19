
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class Dashboard(BasePage):
    logo_scouts_panel_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[1]"
    football_kolektyw_button_xpath = '//*[@title ="Logo Scouts Panel"]'
    main_page_xpath = "//span[text()='Main page']"
    players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_version_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    additional_links_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/h2"
    activity_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h2"
    add_player_xpath = "//span[text()='Add player']"
    last_created_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[1]"
    last_updated_player_xpath = "//a[contains(@href, 'pl/players/64a3002959040b463e2b5ac3/edit')]"
    last_created_match_xpath = "//a[contains(@href, '/pl/players/6026d92156c79737b3f3c62a/edit')]"
    last_updated_match_xpath = "//*[text()='Last updated match']"
    last_updated_report_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[5]"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    expected_title = "Scouts panel - log in"
    add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_a_player_expected_title = "Add player"
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.football_kolektyw_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player(self):
        self.click_on_the_element(self.add_player_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title
