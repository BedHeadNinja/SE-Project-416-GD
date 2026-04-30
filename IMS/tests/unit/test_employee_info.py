import time
from selenium.webdriver.common.by import By

def test_employee_info_navigation(login_driver):
    """
    GIVEN a logged in user
    WHEN navigating the top menu
    THEN check that navigation to the inventory page is successful
    """
    login_driver.find_element(By.ID,"menu-employee-info-button").click()
    assert "employee" in login_driver.current_url.lower()

def test_add_employee_button(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to add an employee
    THEN check that the button is clickable
    """
    login_driver.find_element(By.ID,"add-employee-button").click()
    time.sleep(3)

    assert login_driver.find_element(By.ID,"add-employee-button").is_enabled()

def test_add_employee_visible(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to add an employee
    THEN check that the form is visible
    """

    assert login_driver.find_element(By.ID,"add-employee").is_displayed()

    #def test_add_employee()
    """
    GIVEN a logged in user
    WHEN attempting to add an employee
    THEN check that the form is visible
    """
    #login_driver.find_eBy.ID,"name").send_keys("add_employee_test_name")
    #login_driver.find_eBy.ID,"id").send_keys("4242")
    #login_driver.find_eBy.ID,"role").click()
