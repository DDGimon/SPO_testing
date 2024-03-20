import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import allure
from base.password import get_password
from base.variables import Url
from base.base_class import Base
from utilities.logger import Logger
from utilities.utilities import driver, spo_info


class AuthorizationPage(Base):
    def __init__(self, driver, spo_info):
        super().__init__(driver)
        self.pickle = pickle
        self.driver = driver
        self.action = ActionChains(driver)
        self.password = get_password()
        self.url = Url()
        self.spo_info = spo_info
        self.cookies = pickle.load(open('C:\\Users\\Tester\\SPO_testing\\SPO_test\\cookies\\cookies.pkl', "rb"))

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
        with allure.step('Авторизация на сайте'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url.testing_stand)
            self.driver.maximize_window()
            self.get_current_url()
            self.send_input_login(self.spo_info['login'])
            self.send_input_password(self.password)
            self.click_button_login()
            time.sleep(1)
            self.assert_url(self.url.url_after_authorization)
            self.pickle.dump(self.driver.get_cookies(), open('C:\\Users\\Tester\\SPO_testing\\SPO_test\\cookies\\cookies.pkl', "wb"))
            Logger.add_end_step(url=self.driver.current_url, method='authorization')

    def authorization_with_cookies(self):
        with allure.step('Авторизация с куками'):
            Logger.add_start_step(method='authorization_with_cookies')
            self.driver.get(self.url.testing_stand)
            self.driver.delete_all_cookies()
            for cookie in self.cookies:
                self.driver.add_cookie(cookie)
            self.driver.get(self.url.url_after_authorization)
            self.assert_url(self.url.url_after_authorization)
            Logger.add_end_step(url=self.driver.current_url, method='authorization_with_cookies')