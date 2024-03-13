import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import driver, spo_info

from base.variables import Url
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    def __init__(self, driver, spo_info):
        super().__init__(driver)
        self.spo_info = spo_info
        self.driver = driver
        self.action = ActionChains(driver)
        self.urls = Url()

    # Locators
    button_arm_head = '//div[@class="menu0"]/a[3]'
    button_study_plan = '//div[@class="selection"]/a'
    button_add_plan = '//a[@class="button button--blue button--medium"]'
    form_study_data = '//p[@class="ej-text ej-text--var-heading-2 ej-text--align-left"]'
    profession_study_data = '//p[@class="ej-text ej-text--var-heading-3 ej-text--align-left"]'
    study_level_data = '//p[@class="ej-text ej-text--var-body-2 ej-text--color-secondary ej-text--align-left"]'
    name_plan_data = '//div[@class="N7deZqyBsqTNJw2HUOc6 YPvbZ42QRQEWFeQ1H6Qr"]/div[2]/div/div/div/span/a'
    education_program = '//span[@class="ej-chip ej-chip--size-medium ej-chip--effect-light ej-chip--color-blue"]'

    # Getters
    def get_button_arm_head(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_arm_head)))

    def get_button_study_plan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_study_plan)))

    def get_button_add_plan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_plan)))

    def get_form_study_data(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.form_study_data)))

    def get_profession_study_data(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profession_study_data)))

    def get_study_level_data(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.study_level_data)))

    def get_name_plan_data(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_plan_data)))

    def get_education_program(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.education_program)))

    # Actions
    def click_button_arm_head(self):
        self.get_button_arm_head().click()
        print('Click button arm head')

    def click_button_study_plan(self):
        self.get_button_study_plan().click()
        print('Click button study plan')

    def click_button_add_plan(self):
        self.get_button_add_plan().click()
        print('Click button add plan')

        # Возврат значений плана на главной странице

    def receive_form_study_data(self):
        return self.get_form_study_data().text

    def receive_profession_study_data(self):
        return self.get_profession_study_data().text

    def receive_name_plan_data(self):
        return self.get_name_plan_data().text

    def receive_education_program_data(self):
        return self.get_education_program().text

    def receive_study_level_data(self):
        return self.get_study_level_data().text

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

    # Открытие страницы создания учебного плана
    def open_page_add_plan(self):
        with allure.step('Переход на страницу создания "Учебного плана"'):
            Logger.add_start_step(method='open_page_add_plan')
            self.click_button_add_plan()
            self.get_current_url()
            self.assert_url(self.urls.url_add_plan)
            Logger.add_end_step(url=self.driver.current_url, method='open_page_add_plan')

    # Проверка данных после создание учебного плана

    def check_plans_data(self):
        expected_form_study = self.receive_form_study_data()
        actual_form_study = self.spo_info['form_data']
        assert expected_form_study == actual_form_study
        print('Форма обучения совпадает')

        expected_profession_study = self.receive_profession_study_data()
        actual_profession_study = self.spo_info['profession']
        assert expected_profession_study == actual_profession_study
        print('Проффесия обучения совпадает')

        expected_education_program = self.receive_education_program_data()
        actual_education_program = self.spo_info['education_program']
        assert expected_education_program == actual_education_program
        print('Необходимый уровень образования совпадает')

        expected_name_plan = self.receive_name_plan_data()
        actual_name_plan = self.spo_info['name_plan']
        print(expected_name_plan)
        print(actual_name_plan)
        assert expected_name_plan == actual_name_plan
        print('Название плана совпадает')

        expected_study_level = self.receive_study_level_data().replace('#', '')
        actual_study_level = self.spo_info['study_level']
        assert expected_study_level == actual_study_level
        print('Программа подготовки совпадает')
