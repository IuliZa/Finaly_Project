import pytest
from selenium import webdriver


CHROME_EXECUTABLE_PATH = 'C:\Softwares\Drivers\chromedriver.exe'
BASE_URL = 'https://www.labirint.ru'

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
    driver.maximize_window()

    yield driver

    driver.quit()
