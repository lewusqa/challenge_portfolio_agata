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
    club_field_xpath = "//input[@name='club']"
    submit_button_xpath = "//button[@type='submit']"

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
