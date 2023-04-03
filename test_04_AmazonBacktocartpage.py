from config.Settings import *

def test_back_to_cart_page(setup):
    driver = setup
    driver.back()
    driver.back()
    driver.implicitly_wait(3)
    driver.refresh()
    assert "Amazon.in Shopping Cart" in driver.title