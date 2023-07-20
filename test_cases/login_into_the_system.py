import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.addaplayer import AddAPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_page(self):
        user_login = LoginPage(self.driver)
        time.sleep(3)
        user_login.title_of_page()
        user_login.check_page_header()
        user_login.type_in_email("user02@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.wait_for_element_to_be_clickable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        time.sleep(4)
        dashboard_page.title_of_page()
        time.sleep(4)
        add_player = AddAPlayer(self.driver)
        time.sleep(2)


    @classmethod
    def tearDown(self):
        self.driver.quit()
