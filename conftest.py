import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_size():
    browser.open('data:')
    browser.driver.set_window_size(width=1920, height=1080)


@pytest.fixture()
def init_browser():
    browser.open('https://yandex.ru/')