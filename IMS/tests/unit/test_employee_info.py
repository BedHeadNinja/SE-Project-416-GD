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

def test_add_employee(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to add an employee
    THEN check that the employee is successfully added
    """
    login_driver.find_element(By.ID,"name").send_keys("add_employee_test_name")
    login_driver.find_element(By.ID,"id").send_keys("4242")
    select_element = login_driver.find_element(By.ID,"role")
    select = Select(select_element)
    select.select_by_visible_text('Employee')

    login_driver.find_element(By.ID,"submit").click()

    table = login_driver.find_element(By.ID,"employee-table")
    rows = table.find_elements(By.XPATH,".//tbody/tr")

    for row in rows:
        if "add_employee_test_name" in row.text.lower():
            employee_name = row.text.lower().split()[0]
            break

    assert "add_employee_test_name" in employee_name

def test_remove_employee_button(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to remove an employee
    THEN check that the button is clickable
    """
    login_driver.find_element(By.ID,"remove-employee-button").click()
    time.sleep(3)

    assert login_driver.find_element(By.ID,"remove-employee-button").is_enabled()

def test_remove_employee_visible(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to remove an employee
    THEN check that the form is visible
    """

    assert login_driver.find_element(By.ID,"remove-employee").is_displayed()

def test_remove_employee(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to remove an employee
    THEN check that the employee is successfully remove
    """
    table = login_driver.find_element(By.ID,"employee-table")
    rows = table.find_elements(By.XPATH,".//tbody/tr")

    for row in rows:
        if "add_employee_test_name" in row.text.lower():
            employee_id = row.text.lower().split()[1]
            break

    login_driver.find_element(By.ID,"employee_id").send_keys(employee_id)
    login_driver.find_element(By.ID,"submit").click()

    for row in rows:
        if "add_employee_test_name" in row.text.lower():
            removed_id = row.text.lower().split()[1]
            break

    assert "add_employee_test_name" not in removed_id
