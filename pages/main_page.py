import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.testing_settings import Url
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)
        self.urls = Url()

    # Locators
    button_arm_head = '//div[@class="menu0"]/a[3]'
    button_study_plan = '//div[@class="selection"]/a'

    # Getters
    def get_button_arm_head(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_arm_head)))

    def get_button_study_plan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_study_plan)))

    # Actions
    def click_button_arm_head(self):
        self.get_button_arm_head().click()
        print('Click button arm head')

    def click_button_study_plan(self):
        self.get_button_study_plan().click()
        print('Click button study plan')

    # Methods:

    # Открытие страницы учебного плана
    def open_page_study_plans(self):
        with allure.step('Переход на страницу "Учебный план"'):
            Logger.add_start_step(method='open_page_study_plans')
            self.get_current_url()
            self.click_button_arm_head()
            self.click_button_study_plan()
            self.assert_url(self.urls.url_study_plan)
            Logger.add_end_step(url=self.driver.current_url, method='open_page_study_plans')
