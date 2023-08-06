
from pages.base_page import BasePage
import time
class AddAPlayer(BasePage):
    login_button_xpath = "//*[@id='login']"
    football_kolektyw_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[2]/h2'
    #add_player_xpath = "//*[text()='Add player']"
    #add_player_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    email_xpath = "//div[2]/div/div[1]/div/div/input"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    age_xpath = "//*[@name='age']"
    club_field_xpath = "//input[@name='club']"
    level_xpath = "//input[@name='level']"
    main_position_xpath = "//input[@name='mainPosition']"
    second_position_xpath = "//input[@name='secondPosition']"
    district_xpath = "//input[@name='district']"
    achievements_xpath = "//input[@name='achievements']"
    previous_club_xpath = "//input[@name='prevClub']"
    add_language = "//span[@class='MuiButton-label']"
    laczy_nas_pilka_xpath = "//input[@name='webLaczy']"
    min_xpath = "//input[@name='web90']"
    facebook_xpath = "//input[@name='webFB']"
    add_link_to_youtube_xpath = "//*[text()='Add link to Youtube']"
    submit_button_xpath = "//button[@type='submit']"
    clear_xpath = "//span[text()='Clear']"
    add_a_player_expected_title = "Add player"
    #add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    #dashboard_url = "https://scouts-test.futbolkolektyw.pl/login"
    dashboard_url = "https://dareit.futbolkolektyw.pl/en"
    add_a_player_url = "https://dareit.futbolkolektyw.pl/en/players/add"
    expected_title = "Scouts panel"
    #main_page_xpath = "//span[text()='Main page']"
    def type_in_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_xpath, weight)

    def type_in_club_name(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_previous_club(self,previous_club):
        self.field_send_keys(self.previous_club_xpath, previous_club)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        check_title = self.get_page_title(self.add_a_player_url)
        print("check title:", check_title)
        print("add_a_player_expected_title", self.add_a_player_expected_title)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert check_title == self.add_a_player_expected_title

    #def click_add_player(self):
     #   self.click_on_the_element(self.add_player_xpath)
     #   assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title
    def test_add_a_player_to_database(self):
        add_player = AddAPlayer(self.driver)
        add_player.get_page_title(add_player.add_a_player_url)
        time.sleep(3)

    #def last_created_player(self):
    #    self.click_on_the_element(self.main_page_xpath)