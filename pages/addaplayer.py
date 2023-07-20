import time

from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_player_xpath = "//div/div/a/button/span[1]"
    email_xpath = "//div[2]/div/div[1]/div/div/input"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    age_xpath = "//*[@name='age']"
    #choose_leg
    club_field_xpath = "//input[@name='club']"
    level_xpath = "//input[@name='level']"
    main_position_xpath ="//input[@name='mainPosition']"
    second_position_xpath = "//input[@name='secondPosition']"
    district_xpath= "//input[@name='district']"
    achievements_xpath = "//input[@name='achievements']"
    add_language = "//span[@class='MuiButton-label']"
    laczy_nas_pilka_xpath = "//input[@name='webLaczy']"
    min_xpath = "//input[@name='web90']"
    facebook_xpath = "//input[@name='webFB']"
    add_link_to_youtube_xpath = "//*[text()='Add link to Youtube']"
    submit_button_xpath = "//button[@type='submit']"
    clear_xpath = "//span[text()='Clear']"
    add_a_player_expected_title = "Add player"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def title_of_page(self):
        #time.sleep(2) zastap to waitem
        assert self.get_page_title(self.add_a_player_url) == self.expected_title

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

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
