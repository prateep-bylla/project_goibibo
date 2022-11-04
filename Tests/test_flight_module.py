import datetime
import time
import pytest
from Library.excle_lib import ReadExcle
from POM.flight_module import FlightPage
from Library.config import Configuration

class TestFlightPage:
    obj = ReadExcle()
    data = obj.read_test_data(Configuration.FLIGHT_TEST_DATASHEET)

    @pytest.mark.parametrize("first_name, last_name, email, phone_no, card_no, card_name, expire_date, cvv, from_loc, to_loc", data )
    def test_cheap_flights(self, first_name, last_name, email, phone_no, card_no, card_name, expire_date, cvv, from_loc, to_loc, init_driver):
        driver = init_driver

        try:
            obj = FlightPage(init_driver)
            obj.cheap_flights_btn()
            obj.air_lines_btn()
            obj.schedule_btn()
            obj.oneway_btn()
            obj.from_location_btn(from_loc)
            obj.from_location_text()
            obj.to_location_btn(to_loc)
            obj.to_location_text()
            obj.select_date_btn()
            obj.date_btn()
            obj.view_fairs_btn()
            obj.book_btn()
            obj.insurance_btn()
            obj.title_btn()
            obj.first_name_btn(first_name)
            obj.last_name_btn(last_name)
            obj.email_text(email)
            obj.mobile_no_btn(phone_no)
            obj.proceed_btn()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOTS_PATH+name)
            raise err_msg







#pytest test_flight_module.py -vs
#pytest test_flight_module.py -vs --html=C:\Users\vines\PycharmProjects\Goibibo_pytest\Reports\report.html
