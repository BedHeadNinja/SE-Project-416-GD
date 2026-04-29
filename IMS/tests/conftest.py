import pytest
from IMS import create_app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def app():
    # Create app object
    app = create_app()

    # Set testing to true in config
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture(scope="session")
def driver(request):
    # Create driver object
    driver = webdriver.Firefox()

    # Get the login page
    driver.get("http://127.0.0.1:5000/auth/ID")

    # Make driver wait 10 seconds
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def login_driver(request):
    # Create driver object
    driver = webdriver.Firefox()

    # Get the login page
    driver.get("http://127.0.0.1:5000/auth/ID")

    # Enter ID
    driver.find_element(By.NAME,"username").send_keys("2")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(3)

    # Enter password
    driver.find_element(By.NAME,"password").send_keys("Temporary")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(3)

    # Make driver wait 10 seconds
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

