import inspect


def open_browser(chrome, firefox):
    pass


def go_to_companyname_homepage(ozon, wildberries):
    pass


def find_registration_button_on_login_page():
    pass


def description_of_actions(func):
    arguments = str(inspect.signature(func)).replace("(", "").replace(")", "")
    description = func.__name__.replace("_", " ").capitalize(), arguments
    if len(arguments) > 0:
        print(*description, sep=': ')
    else:
        print(*description)


functions = open_browser, go_to_companyname_homepage, find_registration_button_on_login_page

for i in functions:
    description_of_actions(i)

