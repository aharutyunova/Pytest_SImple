from selenium.webdriver.common.by import By
from lib.helpers import Helper
from collections import defaultdict
from lib.helpers import Helper


class Home(Helper):
    logo = (By.ID, "header_logo")
    btn_login = (By.XPATH, "//a[@class='login']")
    btn_logout = (By.XPATH, "//a[@class='logout']")
    btn_account = (By.XPATH, "//a[@class='account']/span")
    btn_contact_us = (By.XPATH, "//div[@id='contact-link']/a")

    btn_dresses_category = (By.XPATH, "//ul[contains(@class,'menu-content')]/li/a[@title='Dresses']")

    _product_xpath = "//div[@class='product-container']/div[@class='right-block']"
    lbl_product_names = (By.XPATH, f"{_product_xpath}/h5/a")
    lbl_product_prices = (By.XPATH, f"{_product_xpath}//span[@itemprop='price']")

    def click_sign_in(self):
        self.logger("Sign in")
        self.find_and_click(self.btn_login)
        self.wait_for_page("controller=authentication")

    def click_sign_out(self):
        self.logger("Logout")
        self.find_and_click(self.btn_logout)
        self.find(self.btn_login)

    def click_contact_us(self):
        self.logger("Go to 'Contact us' page")
        self.find_and_click(self.btn_contact_us)
        self.wait_for_page("controller=contact")

    def click_dresses_tab(self):
        self.logger("Go to 'Dresses' page")
        self.find_and_click(self.btn_dresses_category)
        self.wait_for_page("id_category=8")

    def get_product_names_and_prices(self):
        result = self.find_all(self.lbl_product_names)
        if result:
            self.logger(f"Found {len(result)} products:")
            names = [i.text for i in result]
            prices = [i.text for i in self.find_all(self.lbl_product_prices)]
            temp = defaultdict(set)
            for a, b in zip(names, prices):
                temp[a].add(b)
            self.logger(dict(temp))
        else:
            self.logger("Products not found!", error=True)



