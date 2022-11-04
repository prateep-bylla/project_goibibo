import pytest
from selenium import webdriver
from Library.config import Configuration

@pytest.fixture(params=["Chrome"]) #"firefox","edge"
def init_driver(request):
    global driver
    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)

    # else:
    #     driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)

    driver.get(Configuration.URL)
    driver.maximize_window()
    yield driver
    driver.close()