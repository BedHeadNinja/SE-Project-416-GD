import time
from selenium.webdriver.common.by import By
from IMS.models import User

def test_loginID_elements_visible(login):
    """
    GIVEN a login page
    WHEN the login page is accessed
    THEN check that all elements on page are visible
    """

    # Check all form elements are visible
    assert login.find_element(By.NAME,"username").is_displayed()
    assert login.find_element(By.CSS_SELECTOR,"input[type='submit']").is_displayed()

def test_login_button_clickable(login):
    """
    GIVEN a login page
    WHEN the login button is clicked
    THEN check that the element is enabled
    """
    login.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(2)
    assert login.find_element(By.CSS_SELECTOR,"input[type='submit']").is_enabled()
    print("Login button is clickable")

    #def test_required_fields(login):
    """
    GIVEN a login page
    WHEN the login button is clicked without inputting required info
    THEN check that an empty field error message is displayed
    """

    #login.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    #error = login.find_element(BY.XPATCH)

def test_successful_ID_entry(login):
    """
    GIVEN a login page with ID entry
    WHEN a valid ID is submitted
    THEN check that the page correctly redirects to password entry
    """
    login.find_element(By.NAME,"username").send_keys("2")
    login.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(5)
    assert "password" in login.current_url.lower()
    print("Successful ID entry")

def test_successful_password_entry(login):
    """
    GIVEN a login page
    WHEN valid login information is entered
    THEN check that login is successful
    """
    login.find_element(By.NAME,"password").send_keys("Temporary")
    login.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(5)
    assert "index" in login.current_url.lower()
    print("Successful login")
