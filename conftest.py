import pytest
from selene.support.shared import browser

@pytest.fixture()
def init_browser():
    browser.open('https://yandex.ru/')