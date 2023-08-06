from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

class Dashboard(BasePage):
    #football_kolektyw_xpath = '//*[@title ="Logo Scouts Panel"]'
    football_kolektyw_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[2]/h2'
    login_button_xpath = "//*[@id='login']"
    main_page_xpath = "//span[text()='Main page']"
    players_xpath = "//div[2]/div[2]/span"
    language_version_xpath = "//*[@class='MuiListItemText-root']/span"
    sign_out_xpath = "//span[text()='Sign out']"
    activity_xpath = "//*[text()='Activity']"
    last_created_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    #add_player_xpath = "//*[text()='Add player']"
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    shortcuts_xpath = "//*[text()='Shortcuts']"
    players_count_xpath = "//*[text()='Players count']"
    matches_count_xpath = "//*[text()='Matches count']"
    reports_count_xpath = "//*[text()='Reports count']"
    events_count_xpath = "//*[text()='Events count']"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel - sign in"
    #expected_title = "Scouts panel"
    #add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    dashboard_url = "https://dareit.futbolkolektyw.pl/en"
    add_a_player_url = "https://dareit.futbolkolektyw.pl/en/players/add"
    add_a_player_expected_title = "Add player"
    wait = WebDriverWait(driver, 10)

    #def title_of_page(self):
        #self.wait_for_element_to_be_clickable(self.login_button_xpath)
        #time.sleep(5)
        #assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player(self):
        self.click_on_the_element(self.add_player_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title

    def title_of_page(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains(self.expected_title))
        actual_title = self.driver.title

        print("Actual Title:", actual_title)
        print("Expected Title:", self.expected_title)

        assert actual_title == self.expected_title, "Page title does not match the expected title."
