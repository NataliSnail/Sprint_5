from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators


'''переход по клику на «Личный кабинет»'''

class TestPersonalAccount:
    def test_go_to_personal_account(self,login):
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        assert WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located((Locators.PROFILE)))
        