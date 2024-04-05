from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_PASSWORD_REGISTRATION1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_PASSWORD_REGISTRATION2 = (By.CSS_SELECTOR, "#id_registration-password2")
