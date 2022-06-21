import pytest
from selene.support.shared import browser
from selene import be, have



@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.open('data:')
    browser.driver.set_window_size(width=1920, height=1080)


@pytest.fixture()
def init_browser():
    browser.open('https://yandex.ru/')


@pytest.fixture()
def add_query():
    browser.element('#text').should(be.blank).type(
        'Selene - User-oriented Web UI browser tests in Python').press_enter()
