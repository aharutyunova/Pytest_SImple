import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from lib.helpers import Helper
from pages.home import Home
from testdata import test_data
from lib.helpers import Helper
import time
from faker import Faker

faker = Faker()

class ContactUs(Helper):
    dd_subject = (By.ID, "id_contact")
    dd_reference = (By.XPATH, "//select[@name='id_order']")
    field_attach_file = (By.ID, "fileUpload")
    txt_message = (By.ID, "message")
    field_email = (By.ID, "email")
    btn_send_message = (By.ID, "submitMessage")
    alert_success = (By.XPATH, "//p[contains(@class,'alert-success')]")
    alert_fail = (By.XPATH, "//div[contains(@class,'alert-danger')]//li")

    def send_message_to_support(self, message=""):
        home_obj = Home(self.driver)
        home_obj.click_contact_us()
        self.logger(f"Send message to support: '{message}'")

        Select(self.find(self.dd_subject)).select_by_index(1)
        
        # self.driver.find_element(*self.field_attach_file).send_keys(
        #     f"{os.getcwd()}/{test_data.log_file_name}")
        self.find_and_send_keys(self.field_email, f"{faker.text(max_nb_chars=6)}@gmail.com")
        self.find_and_send_keys(self.txt_message, message) if message else None
        self.find_and_click(self.btn_send_message)
        alert_text = self.find(
            self.alert_success if message else self.alert_fail, get_text=True)
        if message:
            assert alert_text == "Your message has been successfully sent to our team."
        else:
            assert alert_text == "The message cannot be blank."
