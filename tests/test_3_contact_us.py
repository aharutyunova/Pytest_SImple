from pages.contact_us import ContactUs
from lib.helpers import Helper
from testdata import test_data

def test_3_contact_us_success(driver):
    helper =  Helper(driver)
    helper.go_to_page(test_data.main_url)
    contact_us = ContactUs(driver)
    contact_us.send_message_to_support(message="Some message to support")