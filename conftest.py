import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import Constants
from constants import Urls
from locators import Locators


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Urls.URL)
    yield driver
    driver.quit()

@pytest.fixture
def driver_authorisation_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Urls.URL_AUTHORISATION_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def driver_registration_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Urls.URL_REGISTRATION_PAGE)
    yield driver
    driver.quit()
@pytest.fixture
def login(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.SUBMIT_BUTTON).click()
    return driver