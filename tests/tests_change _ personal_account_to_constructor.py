from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint.constants import Constants
from Sprint.locators import Locators
import time

class TestPersonalAccount:
    def test_click_button_enter_to_account(self,driver):
            '''переход по клику на «Конструктор»'''
            driver.find_element(*Locators.ENTER_TO_ACCOUNT).click()
            driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
            driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
            driver.find_element(*Locators.SUBMIT_BUTTON).click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_ACCOUNT)))
            driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
            driver.find_element(*Locators.CONSTRUCTOR).click()
            assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
            driver.quit()


    def test_click_logo_Stellar_Burgers(self, driver):
            '''переход по клику на логотип Stellar Burgers'''
            driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
            driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
            driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
            driver.find_element(*Locators.SUBMIT_BUTTON).click()
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_ACCOUNT)))
            driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
            driver.find_element(*Locators.LOGO).click()
            assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
            driver.quit()

