from selene.support.shared import browser
from selene import have


def test_search_selene_pass(init_browser, add_query):
    browser.element('#search-result').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_selene_fail(init_browser, add_query):
    browser.element('#search-result').should(have.text('Selen - User-oriented Web UI browser tests in Python'))




