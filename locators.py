from selenium.webdriver.common.by import By
from selenium import webdriver

class Locators:
    NAME_FIELD = (By.XPATH, '//label[contains(text(),"Имя")]/..//input')        #поле Имя
    EMAIL_FIELD = (By.XPATH, '//label[contains(text(),"Email")]/..//input')     #поле Емаил
    PASSWORD_FIELD = (By.XPATH, '//label[contains(text(),"Пароль")]/..//input') #поле Пароль
    REG_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')            #кнопка  Зарегистрироваться
    ERROR_PASSWORD = (By.CLASS_NAME, "input__error")                            #ошибка 'Некорректный пароль'
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')                      #кнопка "Войти"
    SUBMIT_LINK = (By.XPATH,'//a[contains(@href, "/login")]')                   # ссылка "Войти" на странице "Зарегистрироваться"
    ENTER_TO_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')         #кнопка "Войти в аккаунт"
    CHECKOUT = (By.XPATH, '//button[text()="Оформить заказ"]')                  #кнопка "Оформить заказ"
    PERSONAL_ACCOUNT = (By.XPATH, '//a[contains(@href, "/account")]')           #кнопка "Личный кабинет"
    LOGOUT = (By.XPATH, '//button[text()="Выход"]')                             #кнопка "Выход"
    CONSTRUCTOR = (By.XPATH, '//p[contains(text(), "Конструктор")]')            #кнопка "Конструктор"
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')                     #логотип Stellar Burgers
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')    #ссылка "Восстановить пароль"
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')                    #кнопка "Восстановить"
    CODE_RECOVERY_FIELD = (By.XPATH, '//label[contains(text(),"Введите код из письма")]/..//input') #поле "Введите код из письма"
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')                    #кнопка "Сохранить"
    BUNS_BUTTON =  (By.XPATH, '//span[contains(text(), "Булки")]')              # раздел Булки
    ELEMENT_FILLINGS_FIRST = (By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa6f")]')  #элемент Мясо бессмертных моллюсков Protostomia
    SAUCE_BUTTON = (By.XPATH, '//span[contains(text(), "Соусы")]')              #раздел Соусы
    FILLINGS_BUTTON = (By.XPATH, '//span[contains(text(), "Начинки")]')         # раздел Начинки
    PROFILE = (By.XPATH, '//a[contains(@href, "/account/profile")]')            #ссылка "Профиль" в Личном кабинете
    PAGE_LOGIN = (By.CLASS_NAME, 'Auth_login__3hAey')                           #страница авторизации пользователя
    PAGE_RECOVERY = (By.CLASS_NAME, 'Auth_login__3hAey')                        #страница Восстановление пароля
    REGISTRATION_LINK = (By.XPATH, '//a[contains(@href, "/register")]')          #ссылка Зарегистрироваться
    PAGE_SUBMIT = (By.XPATH, '//h2[contains(text(), "Вход")]')                   # страница авторизации https://stellarburgers.nomoreparties.site/login
