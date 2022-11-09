from .base_page import BasePage
from .locators import RegLocators, AuthLocators
import os
import time


class RegPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv('MAIN_URL') or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.link_reg = driver.find_element(*AuthLocators.AUTH_LINK_REG)
        self.first_name = driver.find_element(*RegLocators.REG_FIRST_NAME)
        self.last_name = driver.find_element(*RegLocators.REG_LAST_NAME)
        self.email_or_number = driver.find_element(*RegLocators.REG_EMAIL_OR_NUMBER)
        self.password = driver.find_element(*RegLocators.REG_PASS)
        self.pass_con = driver.find_element(*RegLocators.REG_PASS_CON)
        self.btn = driver.find_element(*RegLocators.REG_BTN)
        self.link_ua1 = driver.find_element(*RegLocators.REG_LINK_UA1)
        self.link_cookie = driver.find_element(*RegLocators.REG_LINK_COOKIE)
        self.link_cp = driver.find_element(*RegLocators.REG_LINK_CP)
        self.link_ua2 = driver.find_element(*RegLocators.REG_LINK_UA2)
        self.link_phone = driver.find_element(*RegLocators.REG_LINK_PHONE)


    def enter_first_name(self, value):
        self.first_name.send_keys(value)

    def enter_last_name(self, value):
        self.last_name.send_keys(value)

    def enter_email_or_number(self, value):
        self.email_or_number.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def enter_pass_con(self, value):
        self.pass_con.send_keys(value)

    time.sleep(3)
