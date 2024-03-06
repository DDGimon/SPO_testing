import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.utilities import driver
from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage


@allure.description('Открытие страницы "Учебный план"')
def test_open_spo_page(set_up, driver):

    ap = AuthorizationPage(driver)
    ap.authorization()
    time.sleep(2)

    mp = MainPage(driver)
    mp.open_page_study_plans()

