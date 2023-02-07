from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time
from whatsapp.config import CHROME_DRIVER_PATH, WHATSAPP_URL


class SendWhatsAppMessage:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get(WHATSAPP_URL)
        print("Wait until screen gets loaded!!")
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.ID, "pane-side"))
        )
        print("Logged In")

    def search_name(self, name, text):
        driver = self.driver
        inp_xpath_search = "//*[@title='Search input textbox']"
        input_box_search = WebDriverWait(driver, 30).until(
            lambda driver: driver.find_element(By.XPATH, inp_xpath_search))
        time.sleep(2)
        input_box_search.send_keys(name + Keys.ENTER)
        time.sleep(2)
        inp_xpath = '//*[@class="selectable-text copyable-text iq0m558w"]'
        input_box = driver.find_element(By.XPATH, inp_xpath)
        time.sleep(2)
        input_box.send_keys(text + Keys.ENTER)
        time.sleep(2)

    def send_message(self, worksheet, message):
        for contact in range(worksheet.nrows):
            name = worksheet.cell_value(contact, 0)
            text = f"hi {name}, {message}"
            print('sending mesage to {}'.format(name))
            self.search_name(name, text)
        self.quit_driver()
    
    def send_msg_to_individual(self, person, message):
        name = person
        if name[0].isalpha(): 
            text = f"hi {name}, {message}"
        else:
            text = f"hi, {message}"
        print('sending mesage to {}'.format(name))
        self.search_name(name, text)
        self.quit_driver()
    
    def send_msg_to_unknown(self, worksheet, message):
        for contact in range(worksheet.nrows):
            number = worksheet.cell_value(contact, 0)
            name = worksheet.cell_value(contact, 0)
            text = f"hi {name}, {message}"
            print('sending mesage to {}'.format(name))
            self.search_name(number, text)
        self.quit_driver()

    def quit_driver(self):
        self.driver.quit()
