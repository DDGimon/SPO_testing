import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.password import get_password
from base.testing_settings import testing_stand, url_after_authorization
from base.base_class import Base


class AuthorizationPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)
        self.url = testing_stand
        self.password = get_password()
        self.url_after_authorization = url_after_authorization

    # Locators
    input_login = '//input[@type="text"]'
    input_password = '//input[@type = "password"]'
    button_login = '//button[@type="submit"]'

    # Getters
    def get_input_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_login)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    # Actions
    def send_input_login(self, text):
        self.get_input_login().send_keys(text)
        print('Input login')

    def send_input_password(self, text):
        self.get_input_password().send_keys(text)
        print('Input password')

    def click_button_login(self):
        self.get_button_login().click()
        print('Click button login')

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.send_input_login('sysadmin')
        self.send_input_password(self.password)
        self.click_button_login()
        time.sleep(1)
        self.assert_url(url_after_authorization)
        self.get_current_url()
