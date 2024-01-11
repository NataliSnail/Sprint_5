from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from Sprint_5.constants import Constants
from Sprint_5.locators import Locators



class TestRegistration:
    def test_incorrect_password(self,driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locators.NAME_FIELD).send_keys(Constants.NAME_FIELD)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.INCORRECT_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()
        error_password= driver.find_element(*Locators.ERROR_PASSWORD)
        error_text = error_password.text
        assert error_text == 'Некорректный пароль'



    def test_valid_password(self,driver_authorisation_page):
        driver_authorisation_page.find_element(*Locators.REGISTRATION_LINK).click()
        driver_authorisation_page.find_element(*Locators.NAME_FIELD).send_keys(Constants.NAME_FIELD)
        driver_authorisation_page.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver_authorisation_page.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver_authorisation_page.find_element(*Locators.REG_BUTTON).click()
        assert driver_authorisation_page.current_url == 'https://stellarburgers.nomoreparties.site/register'
