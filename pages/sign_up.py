from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.home import Home
from lib.helpers import Helper
import random
import string
from faker import Faker
import json

faker = Faker()

class SignUp(Helper):
    txt_new_email = (By.ID, "email_create")
    btn_create_account = (By.ID, "SubmitCreate")
    txt_first_name = (By.ID, "customer_firstname")
    txt_last_name = (By.ID, "customer_lastname")
    txt_email = (By.ID, "email")
    txt_pass = (By.ID, "passwd")
    txt_address1 = (By.ID, "address1")
    txt_city = (By.ID, "city")
    dd_state = (By.XPATH, "//select[@id='id_state']")
    txt_post_code = (By.ID, "postcode")
    txt_mobile = (By.ID, "phone_mobile")
    btn_submit_registration = (By.ID, "submitAccount")

    

    def create_new_account(self, new_email="", new_pass=""):
        home_obj = Home(self.driver)
        new_email = new_email if new_email else f"{faker.text(max_nb_chars=6)}@gmail.com"
        new_pass = new_pass if new_pass else faker.text(max_nb_chars=9)
        home_obj.click_sign_in()
        self.logger(f"Create new account: [{new_email}: {new_pass}]")
        self.find_and_send_keys(self.txt_new_email, new_email)
        self.find_and_click(self.btn_create_account)
        self.wait_for_page("#account-creation")

        self.find_and_send_keys(self.txt_first_name, "first")
        self.find_and_send_keys(self.txt_last_name, "last")
        self.find_and_click(self.txt_email)
        self.find_and_send_keys(self.txt_pass, new_pass)
        self.find_and_send_keys(self.txt_address1, "Some Address")
        self.find_and_send_keys(self.txt_city, "Some City")
        Select(self.find(self.dd_state)).select_by_index(1)
        self.find_and_send_keys(self.txt_post_code, "12345")
        self.find_and_send_keys(self.txt_mobile, "987654321")
        self.find_and_click(self.btn_submit_registration)

        self.wait_for_page("controller=my-account")
        self.find(home_obj.btn_account)
        self.logger("Account created successfully!")
        with open('creds.json', 'w+') as f:
            f.write(json.dumps({'email': new_email, 'pass': new_pass}))
        return new_email, new_pass

