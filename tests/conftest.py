import pytest
from termcolor import colored, cprint

# Вывод текста на каждом методе (Параметры для каждого метода в тесте)
@pytest.fixture()
def set_up():
    print(colored('\n !!!!Start test!!!!', 'blue'))
    yield
    print(colored('\n !!!!Finish test!!!!', 'blue'))


# Вывод текста в начале и конце всего теста (Параметры для всего текста)
@pytest.fixture(scope='module')
def some():
    print('Начало')
    yield
    print('Конец')


# Вывод текста в начале и конце методов (Параметры для всех методов в тесте)
@pytest.fixture(scope='function')
def some_func():
    print('Начало')
    yield
    print('Конец')
