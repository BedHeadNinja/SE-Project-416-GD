import time
from selenium.webdriver.common.by import By
from IMS.models import User

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

    #def test_required_fields(login):
    """
    GIVEN a login page
    WHEN the login button is clicked without inputting required info
    THEN check that an empty field error message is displayed
    """

    #login.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    #error = login.find_element(BY.XPATCH)

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

def test_successful_password_entry(driver):
    """
    GIVEN a login page
    WHEN valid login information is entered
    THEN check that login is successful
    """
    driver.find_element(By.NAME,"password").send_keys("Temporary")
    driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(3)
    assert "index" in driver.current_url.lower()
    print("Successful login")

def test_menu_visibility(driver):
    """
    GIVEN a logged in user
    WHEN clicking on drop-down menu
    THEN check that the menu's content is correctly displayed
    """
    driver.find_element(By.CLASS_NAME,"menu-button").click()
    time.sleep(3)
    assert driver.find_element(By.CLASS_NAME,"menu-button").is_displayed()

def test_inventory_navigation(driver):
    """
    GIVEN a logged in user
    WHEN navigating dropdown menu
    THEN check that navigation to the inventory page is successful
    """
    driver.find_element(By.LINK_TEXT,"Inventory").click()
    assert "inventory" in driver.current_url()
