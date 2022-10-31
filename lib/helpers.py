import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import logging


class Helper:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url, new_window=False):
        if new_window:
            self.driver.execute_script(f"window.open('{url}');")
        else:
            self.driver.get(url)
            self.driver.maximize_window()

    def find_and_click(self, loc, timeout=10):
        elem = self.find(loc, timeout)
        elem.click()

    def find_and_send_keys(self, loc, inp_text, timeout=10):
        elem = self.find(loc, timeout)
        elem.send_keys(inp_text)

    def find(self, loc, timeout=20, should_exist=True, get_text="", get_attribute=""):
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located(loc),
                message=f"Element '{loc}' not found!")
        except Exception as e:
            self.logger(e, error=True)
            if should_exist:
                raise Exception(e)
            return False
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem

    def find_all(self, loc, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_all_elements_located(loc),
                message=f"Elements '{loc}' not found!")
        except Exception as e:
            self.logger(e, error=True)
            return False
        return elements

    def wait_element_disappear(self, loc, timeout=10):
        expected_conditions(self.driver, timeout).until_not(
            expected_conditions.presence_of_element_located(loc))

    def wait_for_page(self, page="", not_page="", timeout=10):
        if page:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.url_contains(page))
        elif not_page:
            WebDriverWait(self.driver, timeout).until_not(
                expected_conditions.url_contains(not_page))

    def switch_window(self, window_id=0):
        self.driver.switch_to.window(self.driver.window_handles[window_id])

    def switch_to_alert(self):
        return self.driver.switch_to.alert


    def logger(self, msg="", error=False):
        logging.basicConfig(
            filename='test_run.txt', filemode='a+', format='%(created)f - %(levelname)s - %(message)s', level=logging.INFO)
        if error:
            logging.error(msg)
        else:
            logging.info(msg)
