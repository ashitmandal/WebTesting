from selenium.webdriver.common.by import By
from Base.selenium_driver import SeleniumDriver
import logging

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    loginLink="Login"
    emailField = "user_email"
    passwordField = "user_password"
    loginButton = "commit"
    #easySearch="search - courses"
    #searchID="search-courses"



    def clickLoginLink(self):
        self.elementClick(self.loginLink,locatorType="link")

    def enterEmail(self,email):
        self.sendKeys(email,self.emailField,locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password,self.passwordField,locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self.loginButton,locatorType="name")

    def login(self,email,password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def validLoginSuccessful(self):

        result=self.isElementPresent(locator="search-courses",locatorType="id")
        return result


    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self.emailField)
        emailField.clear()
        passwordField = self.getElement(locator=self.passwordField)
        passwordField.clear()







