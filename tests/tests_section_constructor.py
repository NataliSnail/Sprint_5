from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from Sprint.constants import Constants
from Sprint.locators import Locators
import time

class TestSectionConstructor:
    def test_buns(self,driver):
        '''тест 'Переход к разделу "Булки"'''
        #Пояснение к шагам теста "Булки":
        #1. элемент "Булки" уже по умолчанию установлен на стартовой странице,поэтому..
        #2. прокрутить страницу вниз, таб переключится с элемента "Булки" на "Начинки"
        #3. Нажать на раздел "Булки", чтобы попасть в нужный раздел,тем самым переключив кнопку

        element = driver.find_element(*Locators.ELEMENT_FILLINGS_FIRST)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*Locators.BUNS_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()


    def test_sauces(self,driver):
        '''тест 'Переход к разделу "Соусы"'''
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()


    def test_filling(self,driver):
        '''тест 'Переход к разделу "Начинки"'''
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()