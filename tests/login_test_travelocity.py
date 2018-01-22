from selenium import webdriver
from pages.login import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):

    _username = "seleniumlogintest@gmail.com"
    _password = "AbcDEH10HHAL"
    _wrongPassword = "ABCDEfgh10"
    baseURL = "https://www.travelocity.com/"

    @pytest.mark.run(order=1)
    def test_ValidLogin(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.login(self._username, self._password)
        result = lp.verifyLoginSuccessful()
        assert result == True
        self.driver.close()

    # Without entering username and password
    @pytest.mark.run(order=2)
    def test_InValidLogin1(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.invalidLogin()
        result = lp.verifyLoginNoUsernameAndPassword()
        assert result == True
        self.driver.quit()

    # incorrect password
    @pytest.mark.run(order=3)
    def test_InValidLogin2(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.login(password=self._wrongPassword)
        result = lp.verifyLoginWrongPassword()
        assert result == True
        self.driver.quit()



# To run from command line
# first, remove:
# firefox = LoginTests()
# firefox.test_validLogin()
# 
# now before to run from command line:
# sudo -H pip uninstall selenium
# sudo -H pip install selenium
# set Gecko Driver in PATH in .bash_profile
# source ~/.bash_profile
# sudo -H pip uninstall pyTest
# sudo -H pip install pyTest

# Run from command line
# py.test
# py.test -s -v tests/login_test_travelocity.py 

