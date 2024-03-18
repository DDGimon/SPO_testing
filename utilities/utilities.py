import base64

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

'''Инициализация драйвера'''


@pytest.fixture
def driver():
    '''Отключаем лишнее логирование'''

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver_chrome = webdriver.Chrome(options=options, service=g)

    '''Обход авторизации из дома'''

    auth = base64.b64encode(b'eljur:kvmpei222').decode()
    driver_chrome.execute_cdp_cmd("Network.enable", {})
    driver_chrome.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Authorization": "Basic " + auth}})

    yield driver_chrome



@pytest.fixture(scope="session")
def spo_info():
    return {
        'login': 'sysadmin',
        'form_data': None,
        'name_plan': 'Тестовое название плана',
        'study_level': None,
        'education_program': None,
        'profession': None

    }
