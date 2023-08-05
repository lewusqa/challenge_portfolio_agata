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
        #self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        #self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        #self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user02@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.wait_for_element_to_be_clickable('//span[text() = "Sign in"]')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(4)
        dashboard_page.click_add_player()
        dashboard_page.wait_for_element_to_be_clickable("//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span")
        time.sleep(2)
        add_player = AddAPlayer(self.driver)
        #add_player.click_add_player()
        #add_player.title_of_page()
        time.sleep(2)
        #self.driver.save_screenshot("")
        #image.open().show()
        #add_player.wait_for_visibility_of_element_located()
        add_player.type_in_name('Agata')
        add_player.type_in_surname('Lewandowska')
        add_player.type_in_phone("+48 655 778 543")
        add_player.type_in_weight("55")
        add_player.type_in_club_name("MisWojtek")
        add_player.type_in_main_position('goalkeeper')
        add_player.type_in_age(35)
        add_player.click_submit_button()
        # dodac sprawdzenie czy player sie dodal na dashboardzie - ostatnio dodany zawodnik
        # czy imie i nazwisko zgadza sie z tym co dodalismy
        time.sleep(6)

    @classmethod
    def tearDown(self):
        self.driver.quit()
