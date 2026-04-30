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
    GIVEN a logged in user with role "manager"
    WHEN attempting to add a product
    THEN check that the form is visible
    """

    assert login_driver.find_element(By.CLASS_NAME,"add-product").is_displayed()

    #def test_add_product(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to add a product
    THEN test that the product is successfully added
    """

    #login_driver.find_element(By.ID,"product_name").send_keys("add_product_test_name")
    #login_driver.find_element(By.ID,"on_hand_count").send_keys("4242")
    #login_driver.find_element(By.ID,"submit").click()

    #table = driver.find_element(By.ID,"tableCSS")
    #rows = table.find_elements(By.XPATH,".//tbody/tr")

    #for row in rows:
    #    if
    #    for cell in row
    #    if row.text.lower().contains("add_product_test_name")
    #        product_name = row.text.lower()
    #        product

    #assert "add_product_test_name" in product_name



