from pages.contact_us import ContactUs
from lib.helpers import Helper
from testdata import test_data
from pages.home import Home

def test_5_woman_dresses(driver):
    helper =  Helper(driver)
    home = Home(driver)
    helper.go_to_page(test_data.main_url)
    home.click_dresses_tab()
    home.get_product_names_and_prices()