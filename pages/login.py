from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "header-account-menu"
    _signin_link = "account-signin"
    _email_field = "signin-loginid"
    _password_field = "signin-password"
    _login_button = "submitButton"
    _successful_login = "header-account-menu-signed-in"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="id")

    def clickSigninLink(self):
        self.elementClick(self._signin_link, locatorType="id")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._successful_login, locatorType="id")
        return result

    def verifyLoginNoUsernameAndPassword(self):
        emailErrorMessage = self.getText("userEmailidError", locatorType="id")
        passwordErrorMessaghe = self.getText("userPasswordError", locatorType="id")
        return (emailErrorMessage == "Please enter your email address.") and (passwordErrorMessaghe == "Please enter password.")

    def verifyLoginWrongPassword(self):
        emailErrorMessage = self.getText("userEmailidError", locatorType="id")
        return (emailErrorMessage == "Please enter your email address.")


    def invalidLogin(self):
        self.clickLoginLink()
        self.clickSigninLink()
        self.clickLoginButton()




