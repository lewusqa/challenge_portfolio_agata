import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.addaplayer import AddAPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.base_page import BasePage
from pages.choose_the_leg import ChooseTheLeg
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
driver = webdriver.Chrome()

class TestChooseTheLeg(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        #self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        #self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        #self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_choose_the_leg(self):
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
        add_player = AddAPlayer(self.driver)
        #time.sleep(2)
        add_player.test_add_a_player_to_database()
        #driver.get("https://dareit.futbolkolektyw.pl/en/players/add")
        #driver.save_screenshot(r"C:\Users\lewan\OneDrive\Dokumenty\GitHub\project\challenge_portfolio_agata\test_cases\screenshots\add_a_player\addaplayer_scrn.png")
        add_player.type_in_name('Agata')
        add_player.type_in_surname('Panek')
        add_player.type_in_phone("+48 655 778 543")
        add_player.type_in_weight("55")
        add_player.type_in_club_name("MisWojtek")
        add_player.type_in_main_position('goalkeeper')
        add_player.type_in_age("30/07/1990")
        add_player.type_in_previous_club("Star Wars")
        select_leg = ChooseTheLeg(self.driver)
        #time.sleep(2)
        select_leg.wait_for_visibility_of_element_located ("//*[@id='mui-component-select-leg']")
        #select_leg.title_of_page()
        select_leg.select_leg("left")

        #driver.save_screenshot(r"C:\Users\lewan\OneDrive\Dokumenty\GitHub\project\challenge_portfolio_agata\test_cases\screenshots\add_a_player\player_added_scrn.png")
        #select_leg = ChooseTheLeg(self.driver)
        #time.sleep(2)
        #select_leg.wait_for_visibility_of_element_located()
        #select_leg.select_leg("right")
        driver.save_screenshot(r"C:\Users\lewan\OneDrive\Dokumenty\GitHub\project\challenge_portfolio_agata\test_cases\screenshots\add_a_player\selected_the_leg_scrn.png")
        select_leg.click_submit_button()
        time.sleep(10)
        #self.click_on_the_element("//span[text()='Main page']")
        select_leg.click_main_page()
        player_name="Agata Panek"
        select_leg.check_last_added_player(player_name)


    @classmethod
    def tearDown(self):
        self.driver.quit()
