from selenium import webdriver
from Pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("ashitmandall@hotmail.com", "matu@123")
        result = self.lp.validLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True