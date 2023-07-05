from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']" "//input[starts-with(@id, "login")]"
    password_field_xpath = "//*[@id="password"]" "//input[@id = "password" and @name="password"]"
    sign_in_button_xpath = "//*[@id="__next"]/form/div/div[2]/button" "//span[text() = "Zaloguj"]"
    remind_passwd_xpath = "//*[@id="__next"]/form/div/div[1]/a" "//a[text()="Przypomnij hasło"]"
    remind_passwd_send_xpath = "//*[@id="__next"]/div[1]/div/div[2]/button/span[1]" "//*[@class="MuiButton-label"]"
    language_version_xpath = "//*[@id="__next"]/form/div/div[2]/div/div"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
