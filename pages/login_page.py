import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[text() = 'Sign in']"
    remind_passwd_xpath = "//*[@id='__next']/form/div/div[1]/a"
    remind_passwd_send_xpath = "//*[@id='__next']/div[1]/div/div[2]/button/span[1]"
    language_version_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    login_url = "https://scouts-test.futbolkolektyw.pl/en/login"
    expected_title = "Scouts panel - sign in"
    title_of_header_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    expected_header_of_box = 'Scouts Panel'
    #add_player_xpath = "//*[text()='Add player']"
    #email_xpath = "//div[2]/div/div[1]/div/div/input"
    #name_xpath = "//*[@name='name']"
    #surname_xpath = "//*[@name='surname']"
    #phone_xpath = "//*[@name='phone']"
    #weight_xpath = "//*[@name='weight']"
    #height_xpath = "//*[@name='height']"
    #club_field_xpath = "//input[@name='club']"
    #submit_button_xpath = "//button[@type='submit']"
    #login_url = "https://dareit.futbolkolektyw.pl/en/login"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.login_field_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_page_header(self):
        self.assert_element_text(self.driver, self.title_of_header_xpath, self.expected_header_of_box)

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