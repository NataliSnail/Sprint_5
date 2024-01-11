from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint.constants import Constants
from Sprint.locators import Locators
import time


class TestLogout:
    def test_logout(self,login):
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located((Locators.LOGOUT))).click()
        assert WebDriverWait(login, 10).until(expected_conditions.visibility_of_element_located((Locators.PAGE_LOGIN)))

