from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint_5.constants import Constants
from Sprint_5.locators import Locators


class TestPersonalAccount:
    def test_click_button_constructor_from_personal_account(self,login):
            '''переход из личного кабинета по клику на «Конструктор»'''
            WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_ACCOUNT))).click()
            login.find_element(*Locators.CONSTRUCTOR).click()
            assert login.current_url == 'https://stellarburgers.nomoreparties.site/'



    def test_click_logo_Stellar_Burgers(self, login):
            '''переход из дичного кабинета по клику на логотип Stellar Burgers'''
            WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located((Locators.PERSONAL_ACCOUNT))).click()
            login.find_element(*Locators.LOGO).click()
            assert login.current_url == 'https://stellarburgers.nomoreparties.site/'


