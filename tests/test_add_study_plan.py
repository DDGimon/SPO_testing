import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_plan_page import AddPlanPage
from utilities.utilities import driver, spo_info
from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage


@allure.description('Cоздание учебного плана')
def test_add_spo_page(set_up, driver, spo_info):

    ap = AuthorizationPage(driver, spo_info)
    ap.authorization_with_cookies()
    time.sleep(2)

    mp = MainPage(driver, spo_info)
    mp.open_page_study_plans()
    mp.open_page_add_plan()

    app = AddPlanPage(driver, spo_info)
    app.add_study_plan()
    time.sleep(9)
    mp.check_plans_data()