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


class AddPlanPage(Base):
    def __init__(self, driver, spo_info):
        super().__init__(driver)
        self.driver = driver
        self.spo_info = spo_info
        self.action = ActionChains(driver)
        self.urls = Url()

    # TODO: Добавить рандомный выбор из нескольких вариантов специальностей через random

    # Locators
    select_profession = '//div[@class="ej-select ej-select--fill"]'
    profession_5 = '//div[@class="ej-select__scroll"]/div[5]'
    selected_profession = '//div[@class="ej-select ej-select--fill"]/div/div'
    input_name_plan = '//input[@placeholder="Введите название"]'

    calendar_start_plan = '//div[@class="ej-datepicker__value"]'
    button_full_time = '//button[@class="button button--white button--medium button--outline yDeRVFxEkXicCbHastxK"][1]'
    button_part_time = '//button[@class="button button--white button--medium button--outline yDeRVFxEkXicCbHastxK"][2]'
    button_distant = '//button[@class="button button--white button--medium button--outline yDeRVFxEkXicCbHastxK"][3]'
    select_start_year = '//div[@class="ej-form-group ej-form-group--3"][1]/div/div'
    start_year_2018 = '//div[@class="ej-form-group ej-form-group--3"][1]/div/div/div/div/div/div[5]'
    select_count_year = '//div[@class="ej-form-group ej-form-group--3"][2]/div/div'
    count_year_5 = '//div[@class="ej-form-group ej-form-group--3"][2]/div/div/div/div/div/div/div[5]'
    select_count_month = '//div[@class="ej-form-group ej-form-group--3"][3]/div/div'
    count_month_5 = '//div[@class="ej-form-group ej-form-group--3"][3]/div/div/div/div/div/div/div[5]'
    select_program = '//div[@class="ej-form-group ej-form-group--6"][1]/div/div'
    general_education = '//div[@class="ej-form-group ej-form-group--6"][1]/div/div/div[2]/div/div/div[1]'
    secondary_education = '//div[@class="ej-form-group ej-form-group--6"][1]/div/div/div[2]/div/div/div[2]'
    selected_education = '//div[@class="ej-form-group ej-form-group--6"]/div/div/div/div'
    select_study_level = '//div[@class="ej-form-group ej-form-group--6"][2]/div/div'
    basic_study = '//div[@class="ej-form-group ej-form-group--6"][2]/div/div/div/div/div/div[1]'
    advanced_study = '//div[@class="ej-form-group ej-form-group--6"][2]/div/div/div/div/div/div[2]'
    study_level = '//div[@class="ej-select__header focus"]/div'
    select_qualification = '//div[@class="ej-form-group ej-form-group--12"][4]/div/div'
    qualification = '//div[@class="ej-form-group ej-form-group--12"][4]/div/div/div[2]/div/div/div[5]'
    button_save = '//button[@class="button button--blue button--medium button--fill"]'

    # Getters
    def get_select_profession(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_profession)))

    def get_selected_profession(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_profession)))

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

    def get_selected_education(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_education)))


    def get_select_study_level(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_study_level)))

    def get_basic_study(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basic_study)))

    def get_advanced_study(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.advanced_study)))

    def get_study_level(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.study_level)))

    def get_select_qualification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_qualification)))

    def get_qualification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.qualification)))

    def get_button_save(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_save)))

    # Actions
    def click_select_profession(self):
        self.get_select_profession().click()
        print('Click select profession')

    def click_profession_5(self):
        self.get_profession_5().click()
        print('Click profession')

    def send_name_plan(self, text):
        self.get_input_name_plan().send_keys(text)
        print('Send name plan')

    def move_to_select_coffee(self):
        self.action.move_to_element(self.get_button_save()).perform()
        print('Move to save button ')

    def click_button_full_time(self):
        self.get_button_full_time().click()
        print('Click button full time')

    # 1
    def save_form_data_text(self):
        form_data = self.get_button_full_time().text
        self.spo_info['form_data'] = form_data
        print('Сохранили форму обучения плана - ' + self.spo_info['form_data'])

    def save_study_level_text(self):
        form_data = self.get_study_level().text
        self.spo_info['study_level'] = form_data
        print('Сохранили уровень подготовки - ' + self.spo_info['study_level'])

    def save_education_text(self):
        form_data = self.get_selected_education().text
        if form_data == 'Среднее общее образование':
            self.spo_info['education_program'] = '11 класс'
        elif form_data == 'Основное общее образование':
            self.spo_info['education_program'] = '9 класс'
        print('Сохранили программу подготовки - ' + self.spo_info['education_program'])

    def save_profession_text(self):
        form_data = self.get_selected_profession().text
        self.spo_info['profession'] = form_data
        print('Сохранили специальность - ' + self.spo_info['profession'])



    def click_select_start_year(self):
        self.get_select_start_year().click()
        print('Click select start year')

    def click_start_year_2018(self):
        self.get_start_year_2018().click()
        print('Click start year 2018')

    def click_select_count_year(self):
        self.get_select_count_year().click()
        print('Click select count year')

    def click_count_year_5(self):
        self.get_count_year_5().click()
        print('Click count year 5')

    def click_select_count_month(self):
        self.get_select_count_month().click()
        print('Click select count month')

    def click_count_month_5(self):
        self.get_count_month_5().click()
        print('Click count month 5')

    def click_select_program(self):
        self.get_select_program().click()
        print('Click select program')

    def click_secondary_education(self):
        self.get_secondary_education().click()
        print('Click secondary_education')

    def click_select_study_level(self):
        self.get_select_study_level().click()
        print('Click select study level')

    def click_basic_study(self):
        self.get_basic_study().click()
        print('Click basic study')

    def click_select_qualification(self):
        self.get_select_qualification().click()
        print('Click select qualification')

    def click_qualification(self):
        self.get_qualification().click()
        print('Click qualification')

    def click_button_save(self):
        self.get_button_save().click()
        print('Click button save')

    # Methods:

    # Создание учебного плана
    def add_study_plan(self):
        with allure.step('Создание "учебного плана"'):
            Logger.add_start_step(method='add_study_plan')
            self.click_select_profession()
            self.click_profession_5()
            self.save_profession_text()
            self.send_name_plan(self.spo_info['name_plan'])
            self.move_to_select_coffee()
            self.save_form_data_text()
            self.click_button_full_time()
            self.click_select_start_year()
            self.click_start_year_2018()
            self.click_select_count_year()
            self.click_count_year_5()
            self.click_select_count_month()
            self.click_count_month_5()
            self.click_select_program()
            self.click_secondary_education()
            self.save_education_text()
            self.click_select_study_level()
            self.click_basic_study()
            self.save_study_level_text()
            self.click_select_qualification()
            self.click_qualification()
            self.click_button_save()
            self.assert_url(self.urls.url_study_plan)

            Logger.add_end_step(url=self.driver.current_url, method='add_study_plan')

    # Открытие страницы учебного плана
