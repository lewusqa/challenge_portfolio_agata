import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.addaplayer import AddAPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.choose_the_leg import ChooseTheLeg
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class ChooseTheLeg(unittest.TestCase):
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

    def test_choose_the_leg(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user02@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        #dashboard_page.title_of_page()
        #time.sleep(4)
        dashboard_page.click_add_player()
        dashboard_page.wait_for_element_to_be_clickable()
        add_player = AddAPlayer(self.driver)
        #add_player.click_add_player()
        add_player.title_of_page()
        time.sleep(2)
        select_leg = ChooseTheLeg(self.driver)
        #self.driver.save_screenshot("")
        #image.open().show()
        select_leg.title_of_page()
        select_leg.wait_for_visibility_of_element_located()
        select_leg.select_leg("right")
        select_leg.click_submit_button()
        # dodac sprawdzenie czy player sie dodal na dashboardzie - ostatnio dodany zawodnik
        # czy imie i nazwisko zgadza sie z tym co dodalismy
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
