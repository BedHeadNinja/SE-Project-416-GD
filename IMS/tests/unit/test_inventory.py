import time
from selenium.webdriver.common.by import By
from IMS.models import User

def test_menu_visibility(login_driver):
    """
    GIVEN a logged in user
    WHEN clicking on drop-down menu
    THEN check that the menu's content is correctly displayed
    """
    login_driver.find_element(By.CLASS_NAME,"menu-button").click()
    time.sleep(3)
    assert login_driver.find_element(By.CLASS_NAME,"menu-button").is_displayed()

def test_inventory_navigation(login_driver):
    """
    GIVEN a logged in user
    WHEN navigating dropdown menu
    THEN check that navigation to the inventory page is successful
    """
    login_driver.find_element(By.LINK_TEXT,"Inventory").click()
    assert "inventory" in login_driver.current_url.lower()

def test_add_product_button(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to add a product
    THEN check that the button is clickable
    """
    login_driver.find_element(By.ID,"add-product-button").click()
    time.sleep(3)

    assert login_driver.find_element(By.ID,"add-product-button").is_enabled()

def test_add_product_visible(login_driver):
    """
    GIVEN a logged in user
    WHEN attempting to add a product
    THEN check that the form is visible
    """

    assert login_driver.find_element(By.CLASS_NAME,"add-product").is_displayed()

    #def test_add_product(login_driver):
    """
    GIVEN a
    WHEN
    THEN
    """
