import re
import time

from Library.excle_lib import ReadExcle
from Library.config import Configuration

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


class FlightPage:

    obj_1 = ReadExcle()
    locator_reg = obj_1.read_locator(Configuration.FLIGHT_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def cheap_flights_btn(self):
        locator = self.locator_reg["cheap_flights_btn"]
        self.driver.find_element(*locator).click()

    def air_lines_btn(self):
        locator = self.locator_reg["air_lines_btn"]
        self.driver.find_element(*locator).click()

    def schedule_btn(self):
        locator = self.locator_reg["schedule_btn"]
        self.driver.find_element(*locator).click()

    def oneway_btn(self):
        locator = self.locator_reg["oneway_btn"]
        self.driver.find_element(*locator).click()

    def from_location_btn(self, from_loc):
        locator = self.locator_reg["from_location_btn"]
        self.driver.find_element(*locator).clear()
        time.sleep(1)
        self.driver.find_element(*locator).send_keys(from_loc)

    def from_location_text(self):
        self.driver.implicitly_wait(10)
        locator = self.locator_reg["from_location_text"]
        self.driver.find_element(*locator).click()

    def to_location_btn(self, to_loc):
        locator = self.locator_reg["to_location_btn"]
        self.driver.find_element(*locator).clear()
        time.sleep(1)
        self.driver.find_element(*locator).send_keys(to_loc)

    def to_location_text(self):
        self.driver.implicitly_wait(10)
        locator = self.locator_reg["to_location_text"]
        self.driver.find_element(*locator).click()

    def select_date_btn(self):
        locator = self.locator_reg["select_date_btn"]
        self.driver.find_element(*locator).click()

    def date_btn(self):
        locator = self.locator_reg["date_btn"]
        self.driver.find_element(*locator).click()

    def view_fairs_btn(self):
        locator = self.locator_reg["view_fairs_btn"]
        self.driver.find_element(*locator).click()

    def book_btn(self):
        element = self.driver.find_element("xpath", '//input[@value="BOOK"]')
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        handles_1 = self.driver.window_handles
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(handles_1[1])

    def insurance_btn(self):
        locator = self.locator_reg["insurance_btn"]
        self.driver.find_element(*locator).click()

    def title_btn(self):
        drop_down = self.driver.find_element("xpath", '//select[@class="common-elementsstyles__CustSelectTrvl-sc-ilw4bs-9 hyDeWs"]')
        dr = Select(drop_down)
        dr.select_by_value("Mr")

    def first_name_btn(self,first_name):
        pattern = r'[A-Z][a-z]*'
        result = re.findall(pattern, first_name)
        assert result, "invalid first Name"
        locator = self.locator_reg["first_name_btn"]
        self.driver.find_element(*locator).send_keys(first_name)

    def last_name_btn(self,last_name):
        pattern = r'[A-Z][a-z]*'
        result = re.findall(pattern, last_name)
        assert result, "invalid last Name"
        locator = self.locator_reg["last_name_btn"]
        self.driver.find_element(*locator).send_keys(last_name)

    def email_text(self,email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email)
        assert result, "invalid email"
        locator = self.locator_reg["email_text"]
        self.driver.find_element(*locator).send_keys(email)

    def mobile_no_btn(self,phone_no):
        if isinstance(phone_no,float):
            phone_no = str(int(phone_no))
        assert len(phone_no) == 10, "invalid number"
        locator = self.locator_reg["mobile_no_btn"]
        self.driver.find_element(*locator).send_keys(phone_no)

    def proceed_btn(self):
        locator = self.locator_reg["proceed_btn"]
        self.driver.find_element(*locator).click()







































































































