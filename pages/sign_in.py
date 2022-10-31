from selenium.webdriver.common.by import By
from pages.home import Home
from testdata import test_data
from lib.helpers import Helper


class SignIn(Helper):
    txt_email = (By.ID, "email")
    txt_pass = (By.ID, "passwd")
    btn_login = (By.XPATH, "//button[@id='SubmitLogin']")

    def login(self, email="", password=""):
        home_obj = Home(self.driver)
        email = email if email else test_data.email_data
        password = password if password else test_data.pass_data
        home_obj.click_sign_in()
        self. logger(f"Login with user: [{email} : {password}]")
        self.find_and_send_keys(self.txt_email, email)
        self.find_and_send_keys(self.txt_pass, password)
        self.find_and_click(self.btn_login)
        self.wait_for_page("controller=my-account")
        self.find(home_obj.btn_account)
