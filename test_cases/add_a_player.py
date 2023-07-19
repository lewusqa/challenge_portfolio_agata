import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.addaplayer import AddAPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user02@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        time.sleep(4)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player()
        time.sleep(4)

        add_player = AddAplayer(self.driver)
        #add_player.click_add_player()
        add_player.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
