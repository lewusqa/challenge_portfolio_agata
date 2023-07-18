import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[text() = 'Sign in']"
    remind_passwd_xpath = "//*[@id='__next']/form/div/div[1]/a"
    remind_passwd_send_xpath = "//*[@id='__next']/div[1]/div/div[2]/button/span[1]"
    language_version_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel - sign in"
    title_of_header_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    excepted_header_of_box = 'Scouts panel - sign in'
    add_player_xpath = "//span[text()='Add player']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        time.sleep(2)
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_page_header(self):
        self.assert_element_text(self.driver, self.title_of_header_xpath, self.excepted_header_of_box)
