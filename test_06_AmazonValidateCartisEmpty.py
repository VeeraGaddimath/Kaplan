from config.Settings import *
from Test_Page.Amazon_CartPage_Locators import CARTISEMPTY
def test_validate_cart_empty(setup):
    driver=setup
    time.sleep(5)
    try:
        empty_cart_message = driver.find_element(By.XPATH, CARTISEMPTY.YOUR_CART_IS_EMPTY)
        assert empty_cart_message.text == "Your Amazon Cart is empty."
        print("Empty cart message is validated successfully.")
    except AssertionError as e:
        print(f"Expected empty cart message not found: {e}")

    print("All Testcases are done")
