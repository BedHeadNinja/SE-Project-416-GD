import time
from selenium.webdriver.common.by import By
from IMS.models import Product

#def test_menu_visibility(login_driver):
#    """
#    GIVEN a logged in user
#    WHEN clicking on drop-down menu
#    THEN check that the menu's content is correctly displayed
#    """
#    login_driver.find_element(By.CLASS_NAME,"menu-button").click()
#    time.sleep(3)
#    assert login_driver.find_element(By.CLASS_NAME,"menu-button").is_displayed()

def test_inventory_navigation(login_driver):
    """
    GIVEN a logged in user
    WHEN navigating the top menu
    THEN check that navigation to the inventory page is successful
    """
    login_driver.find_element(By.ID,"menu-inventory-button").click()
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

def test_add_product(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to add a product
    THEN check that the product is successfully added
    """
    login_driver.find_element(By.ID,"product_name").send_keys("add_product_test_name")
    login_driver.find_element(By.ID,"on_hand_count").send_keys("4242")
    login_driver.find_element(By.ID,"submit").click()

    table = login_driver.find_element(By.ID,"inventory-table")
    rows = table.find_elements(By.XPATH,".//tbody/tr")

    for row in rows:
        if "add_product_test_name" in row.text.lower():
            product_name = row.text.lower()
            break

    assert "add_product_test_name" in product_name

def test_remove_product_button(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to remove a product
    THEN check that the button is clickable
    """
    login_driver.find_element(By.ID,"remove-product-button").click()
    time.sleep(3)

    assert login_driver.find_element(By.ID,"remove-product-button").is_enabled()

def test_remove_product_visible(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to remove a product
    THEN check that the product is successfully added
    """

    assert login_driver.find_element(By.CLASS_NAME,"remove-product").is_displayed()

def test_remove_product(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to remove a product
    THEN check that the product is successfully added
    """
    table = login_driver.find_element(By.ID,"inventory-table")
    rows = table.find_elements(By.XPATH,".//tbody/tr")

    for row in rows:
        if "add_product_test_name" in row.text.lower():
            product_id = row.text.lower().split()[0]
            break

    login_driver.find_element(By.ID,"product_id").send_keys(product_id)
    login_driver.find_element(By.NAME,"submit").click()

    for row in rows:
        if "add_product_test_name" in row.text.lower():
            product_name = row.text.lower()
            break

    assert "add_product_test_name" not in product_name

def test_update_quantity_button(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to update a product quantity
    THEN check that the button is clickable
    """
    login_driver.find_element(By.ID,"update-quantity-button").click()
    time.sleep(3)

    assert login_driver.find_element(By.ID,"update-quantity-button").is_enabled()

def test_update_quantity_visible(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to update a product quantity
    THEN check that the form is visible
    """

    assert login_driver.find_element(By.CLASS_NAME,"update-quantity").is_displayed()

def test_update_quantity(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to update a product quantity
    THEN check that the product quantity is successfully updated
    """
    table = login_driver.find_element(By.ID,"inventory-table")
    rows = table.find_elements(By.XPATH,".//tbody/tr")

    for row in rows:
        if "add_product_test_name" in row.text.lower():
            product_id = row.text.lower().split()[0]
            break

    login_driver.find_element(By.ID,"product_id").send_keys(product_id)
    login_driver.find_element(By.ID,"on_hand_count").send_keys("76")
    login_driver.find_element(By.ID,"submit").click()

    for row in rows:
        if "add_product_test_name" in row.text.lower():
            productQuantity = row.text.lower().split()[3]
            break

    assert "76" in productQuantity

def test_set_threshold_button(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to set a low stock warning threshold
    THEN check that the button is clickable
    """
    login_driver.find_element(By.ID,"set-threshold-button").click()
    time.sleep(3)

    assert login_driver.find_element(By.ID,"set-threshold-button").is_enabled()

def test_set_threshold_visible(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to set a low stock warning threshold
    THEN check that the form is visible
    """

    assert login_driver.find_element(By.CLASS_NAME,"set-threshold").is_displayed()

def test_set_threshold(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to set a low stock warning threshold
    THEN check that the low stock warning threshold is successfully added
    """
    table = login_driver.find_element(By.ID,"inventory-table")
    rows = table.find_elements(By.XPATH,".//tbody/tr")

    for row in rows:
        if "add_product_test_name" in row.text.lower():
            product_id = row.text.lower().split()[0]
            break

    login_driver.find_element(By.ID,"product_id").send_keys(product_id)
    login_driver.find_element(By.ID,"stock_alert_minimum").send_keys("4242")
    login_driver.find_element(By.ID,"submit").click()

    for row in rows:
        if "add_product_test_name" in row.text.lower():
            stockAlert = row.text.lower().split()[-1]
            break

    assert "4242" in stockAlert

def order_product_button(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to order a product
    THEN check that the button is clickable
    """
    login_driver.find_element(By.ID,"order-product-button").click()
    time.sleep(3)

    assert login_driver.find_element(By.ID,"order-product-button").is_enabled()

def order_product_visible(login_driver):
    """
    GIVEN a logged in user with role "manager"
    WHEN attempting to order a product
    THEN check that the form is visible
    """

    assert login_driver.find_element(By.CLASS_NAME,"order-product").is_displayed()

    #def order_product(login_driver):
