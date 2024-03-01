import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage


@allure.description('Открытие страницы "Учебный план"')
def test_open_spo_page(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    ap = AuthorizationPage(driver)
    ap.authorization()
    time.sleep(2)

    mp = MainPage(driver)
    mp.open_page_study_plans()

