import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.utilities import driver
from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage


@allure.description('Переход на страницу добавления учебного плана')
def test_open_add_spo_page(set_up, driver):

    ap = AuthorizationPage(driver)
    ap.authorization()
    time.sleep(2)

    mp = MainPage(driver)
    mp.open_page_study_plans()
    mp.open_page_add_plan()
    mp.receive_form_study_data()

