from pages.reg_page import RegPage
import time


def test_contents_reg_page(driver):
    page = RegPage(driver)
    page.link_reg.click()
    page.driver.save_screenshot('Reg_page.png')
