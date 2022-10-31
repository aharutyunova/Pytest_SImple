from selenium import webdriver
from testdata import test_data
from pages.home import Home
from pages.contact_us import ContactUs
from lib.helpers import Helper
from pages.sign_in import SignIn
from pages.sign_up import SignUp

def test_1_registration(driver):
    sign_up = SignUp(driver)
    helper = Helper(driver)
    helper.go_to_page(test_data.main_url)
    sign_up.create_new_account()



