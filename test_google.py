from selene.support.shared import browser
from selene import be, have


def test_first():
    browser.open('https://yandex.ru/')
    browser.element('#text').should(be.blank).type(
        'Selene - User-oriented Web UI browser tests in Python').press_enter()
    browser.element('#search-result').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

