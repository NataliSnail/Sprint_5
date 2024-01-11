from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from Sprint_5.constants import Constants
from Sprint_5.constants import Urls
from Sprint_5.locators import Locators


class TestAuthorization:
    def test_click_button_enter_to_account(self,driver):
        '''авторизация через кнопку "Войти в аккаунт"'''
        driver.find_element(*Locators.ENTER_TO_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        #использую элемент "Оформить заказ" как подтверждение, что авторизация пройдена, т.к. без авторизации он недоступен
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.CHECKOUT)))



    def test_click_button_personal_account(self, driver):
        '''авторизация через кнопку "Личный кабинет"'''
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        # использую элемент "Оформить заказ" как подтверждение, что авторизация пройдена, т.к. без авторизации он недоступен
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.CHECKOUT)))


    def test_click_forgot_password(self,driver_authorisation_page):
        '''вход через кнопку "Восстановить пароль" в форме восстановления пароля'''
        driver_authorisation_page.find_element(*Locators.FORGOT_PASSWORD).click()
        driver_authorisation_page.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver_authorisation_page.find_element(*Locators.RECOVERY_BUTTON).click()

        WebDriverWait(driver_authorisation_page, 5).until(expected_conditions.visibility_of_element_located((Locators.PASSWORD_FIELD)))
        driver_authorisation_page.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver_authorisation_page.find_element(*Locators.CODE_RECOVERY_FIELD).send_keys(Constants.CODE_RECOVERY_PASSWORD)
        WebDriverWait(driver_authorisation_page, 5).until(expected_conditions.visibility_of_element_located((Locators.SAVE_BUTTON))).click()
        assert driver_authorisation_page.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'


    def test_login_button_on_the_registration_form(self,driver_registration_page):
        '''вход через кнопку 'Войти' на форме регистрации на странице https://stellarburgers.nomoreparties.site/register '''
        driver_registration_page.find_element(*Locators.SUBMIT_LINK).click()
        driver_registration_page.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver_registration_page.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver_registration_page.find_element(*Locators.SUBMIT_BUTTON).click()
        # использую элемент "Оформить заказ" как подтверждение, что авторизация пройдена, т.к. без авторизации он недоступен
        assert WebDriverWait(driver_registration_page, 5).until(expected_conditions.visibility_of_element_located((Locators.CHECKOUT)))
