from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        assert login_link, "LOGIN_LINK is not presented"
        login_link.click()

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL), "LOGIN_EMAIL is not presented"
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD), "LOGIN_PASSWORD is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_REGISTRATION1), "LOGIN_PASSWORD_REGISTRATION1 is not presented"
        assert self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_REGISTRATION2), "LOGIN_PASSWORD_REGISTRATION2 is not presented"
