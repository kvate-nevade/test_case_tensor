import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def download_dir():
    """Определяет папку для загрузки файлов."""
    project_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.join(project_dir, "downloads")
    os.makedirs(download_path, exist_ok=True)
    return download_path

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default = 'en',
                     help="Choose language: ru, en or other..")
    

@pytest.fixture(scope = 'function')
def browser(request, download_dir):
    browser_name = request.config.getoption('browser_name')
    browser_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        options = Options()
        options.add_experimental_option('prefs',{
                                                'intl.accept_languages': browser_language,
                                                "download.default_directory": download_dir,
                                                "download.prompt_for_download": False,
                                                "safebrowsing.enabled": True
                                                 })
        print(f"Задается папка загрузки: {download_dir}")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.implicitly_wait(10)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError('--browser_name shouild be chrome or firefox')
    
    yield browser  # Объект браузера передается в тест

    print('\nbrowser is quiting..')
    browser.quit()
