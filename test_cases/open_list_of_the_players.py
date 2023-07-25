import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.open_list_of_players import OpenListOfPlayers
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestOpenListOfPlayers(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        #self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        #self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_open_list_of_players(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user02@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(4)
        open_list = OpenListOfPlayers(self.driver)
        open_list.click_list_of_players()
        open_list.title_of_page()
        time.sleep(2)
        # dodac sprawdzenie czy player sie dodal na dashboardzie - ostatnio dodany zawodnik
        # czy imie i nazwisko zgadza sie z tym co dodalismy
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
