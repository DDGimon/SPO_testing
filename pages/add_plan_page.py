import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import driver

from base.testing_settings import Url
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)
        self.urls = Url()

    # TODO: Добавить рандомный выбор из нескольких вариантов специальностей через random

    # Locators
    select_profession = '//div[@class="ej-select ej-select--fill"]'
    profession_5 = '//div[@class="ej-select__scroll"]/div[5]'
    input_name_plan = '//input[@placeholder="Введите название"]'
    calendar_start_plan = '//div[@class="ej-datepicker__value"]'
    button_full_time = '//*[@id="content"]/div/div[2]/div/div[1]/div[4]/div/div/button[1]'
    button_part_time = '//*[@id="content"]/div/div[2]/div/div[1]/div[4]/div/div/button[2]'
    button_distant = '//*[@id="content"]/div/div[2]/div/div[1]/div[4]/div/div/button[3]'
    select_start_year = '//div[@class="ej-form-group ej-form-group--3"][1]/div/div'
    start_year_2018 = '//div[@class="ej-form-group ej-form-group--3"][1]/div/div/div[2]/div/div/div[5]'
    select_count_year = '//div[@class="ej-form-group ej-form-group--3"][2]/div/div'
    count_year_5 = '//div[@class="ej-form-group ej-form-group--3"][2]/div/div/div[2]/div/div/div[5]'
    select_count_month = '//div[@class="ej-form-group ej-form-group--3"][3]/div/div'
    count_month_5 = '//div[@class="ej-form-group ej-form-group--3"][3]/div/div/div[2]/div/div/div[5]'
    select_program = '//div[@class="ej-form-group ej-form-group--6"][1]/div/div'
    general_education = '//div[@class="ej-form-group ej-form-group--6"][1]/div/div/div/div/div/div[1]'
    secondary_education = '//div[@class="ej-form-group ej-form-group--6"][2]/div/div/div/div/div/div[1]'
    select_study_level = '//div[@class="ej-form-group ej-form-group--6"][2]/div/div'
    basic_study = '//div[@class="ej-form-group ej-form-group--6"][2]/div/div/div/div/div/div[1]'
    advanced_study = '//div[@class="ej-form-group ej-form-group--6"][2]/div/div/div/div/div/div[2]'
    select_qualification = '//div[@class="ej-form-group ej-form-group--12"][3]/div/div/div/div/'
    qualification = '//div[@class="ej-form-group ej-form-group--12"][3]/div/div/div/div/div/div[5]'
    button_save = '//button[@class="button button--blue button--medium button--fill"]'

    # Getters
    def get_select_profession(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_profession)))

    def get_profession_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profession_5)))

    def get_input_name_plan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_name_plan)))

    def get_calendar_start_plan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calendar_start_plan)))

    def get_button_full_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_full_time)))

    def get_button_part_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_part_time)))

    def get_button_distant(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_distant)))

    def get_select_start_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_start_year)))

    def get_start_year_2018(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_year_2018)))

    def get_select_count_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_count_year)))

    def get_count_year_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.count_year_5)))

    def get_select_count_month(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_count_month)))

    def get_count_month_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.count_month_5)))

    def get_select_program(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_program)))

    def get_secondary_education(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.secondary_education)))

    def get_general_education(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.general_education)))

    def get_select_study_level(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_study_level)))

    def get_basic_study(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basic_study)))

    def get_advanced_study(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.advanced_study)))

    def get_select_qualification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_qualification)))

    def get_qualification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.qualification)))

    def get_button_save(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_save)))

    # Actions
    def click_button_arm_head(self):
        self.get_button_arm_head().click()
        print('Click button arm head')

    # Methods:

    # Открытие страницы учебного плана
    def open_page_study_plans(self):
        with allure.step('Переход на страницу "Учебный план"'):
            Logger.add_start_step(method='open_page_study_plans')
            self.assert_url(self.urls.url_add_plan)
            Logger.add_end_step(url=self.driver.current_url, method='open_page_study_plans')
