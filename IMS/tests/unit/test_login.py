import time
from selenium.webdriver.common.by import By
from IMS.models import User

"""                                 """
#                                     #
#         MODULE: test_login          #
#   Comprehensive testing suite for   #
#      the system's login feature     #
#                                     #
"""                                 """

def test_loginID_elements_visible(driver):
    """
    GIVEN a login page
    WHEN the login page is accessed
    THEN check that all elements on page are visible
    """

    # Check all form elements are visible
    assert driver.find_element(By.NAME,"username").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR,"input[type='submit']").is_displayed()

def test_login_button_clickable(driver):
    """
    GIVEN a login page
    WHEN the login button is clicked
    THEN check that the element is enabled
    """
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR,"input[type='submit']").is_enabled()
    print("Login button is clickable")

def test_ID_required(driver):
    """
    GIVEN a login page with ID entry
    WHEN the login button is clicked without inputting required info
    THEN check that an empty field error message is displayed
    """

    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    error = driver.find_element(By.CSS_SELECTOR,"input#username[name='username']").get_attribute("validationMessage")
    assert "Please fill out this field" in error

def test_invalid_ID_entry(driver):
    """
    GIVEN a login page with ID entry
    WHEN an invalid ID is submitted
    THEN check that an appropriate error message is printed
    """
    driver.find_element(By.NAME,"username").send_keys("-1")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(3)
    error = driver.find_element(By.CLASS_NAME,"errors").text.lower()
    assert "invalid id" in error
    print("Successful ID error print")

def test_successful_ID_entry(driver):
    """
    GIVEN a login page with ID entry
    WHEN a valid ID is submitted
    THEN check that the page correctly redirects to password entry
    """
    driver.find_element(By.NAME,"username").send_keys("2")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(3)
    assert "password" in driver.current_url.lower()
    print("Successful ID entry")

    #def test_loginPassword_elements_visible()

def test_password_required(driver):
    """
    GIVEN a login page with password entry
    WHEN the login button is clicked without inputting required info
    THEN check that an empty field error message is displayed
    """

    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    error = driver.find_element(By.CSS_SELECTOR,"input#password[name='password']").get_attribute("validationMessage")
    assert "Please fill out this field" in error

def test_invalid_password_entry(driver):
    """
    GIVEN a login page
    WHEN an invalid password is submitted
    THEN check that an appropriate error message is printed
    """
    driver.find_element(By.NAME,"password").send_keys("invalid")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(3)
    error = driver.find_element(By.CLASS_NAME,"errors").text.lower()
    assert "invalid password" in error
    print("Successful password error print")

def test_successful_password_entry(driver):
    """
    GIVEN a login page
    WHEN a valid password is submitted
    THEN check that login is successful
    """
    driver.find_element(By.NAME,"password").send_keys("Temporary")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(3)
    assert "index" in driver.current_url.lower()
    print("Successful login")

def test_logout(driver):
    """
    GIVEN a logged-in user
    WHEN the logout button is selected
    THEN check that the user is successfully logged out
    """

    assert driver.find_element(By.ID,"menu-logout-button").is_displayed()

    driver.find_element(By.ID,"menu-logout-button").click()
    time.sleep(3)

    assert "id" in driver.current_url.lower()

def test_login_redirect(driver):
    """
    GIVEN a two-step login page
    WHEN an invalid password is submitted 3 times
    THEN check that the user is redirected to the ID login step
    """

    driver.find_element(By.NAME,"username").send_keys("2")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(3)

    for i in range(3):
        driver.find_element(By.NAME,"password").send_keys("invalid")
        driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
        time.sleep(3)

    assert "id" in driver.current_url.lower()

def test_login_lockout(driver):
    """
    GIVEN a two-step login page
    WHEN a user has been redirected to the ID login step for submitting an invalid password 3 times
    THEN chek that the user is restricted from attempting to log in
    """

    driver.find_element(By.NAME,"username").send_keys("2")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(3)

    error = driver.find_element(By.CLASS_NAME,"errors").text.lower()

    assert "you have reached the maximum number of login attempts" in error
