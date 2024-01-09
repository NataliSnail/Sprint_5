from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint.constants import Constants
from Sprint.locators import Locators
import time


class TestLogout:
    def test_logout(self,driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.LOGOUT)))
        driver.find_element(*Locators.LOGOUT).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.PAGE_LOGIN)))
        driver.quit()

