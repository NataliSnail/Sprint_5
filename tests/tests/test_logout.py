from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import Constants
from locators import Locators



class TestLogout:
    def test_logout(self,login):
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located((Locators.LOGOUT))).click()
        assert WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located((Locators.SUBMIT_AUTHORIZATION)))






