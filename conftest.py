import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     help="Choose language: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if not language:
        raise pytest.UsageError("--language should be entered")

    print(f"\nstart chrome browser with language {language.upper()} for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language.lower()})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
