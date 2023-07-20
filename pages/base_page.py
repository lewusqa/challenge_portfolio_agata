import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    #sprawdzic to
    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(3)

    def wait_for_visibility_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        time.sleep(3)
    @classmethod
    def setUp(cls, self):
        pass
