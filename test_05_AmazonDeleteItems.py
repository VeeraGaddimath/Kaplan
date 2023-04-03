from config.Settings import *
from Test_Page.Amazon_CartPage_Locators import DELETEITEMS

def test_delete_all_items_in_cart(setup):
    driver=setup
    delete_button_xpath = DELETEITEMS.DELETE_ITEMS_CART
    items_in_cart = driver.find_elements(By.XPATH, delete_button_xpath)
    if len(items_in_cart) > 0:
        while len(items_in_cart) > 0:
            time.sleep(5)
            item = items_in_cart[0]
            delete_button = driver.find_element(By.XPATH, delete_button_xpath)
            time.sleep(5)
            delete_button.click()
            WebDriverWait(driver, 5).until(EC.staleness_of(item))
            items_in_cart = driver.find_elements(By.XPATH, delete_button_xpath)
            driver.refresh()
            if len(items_in_cart) == 0:  # check if condition is satisfied
                break  # break out of the loop if condition is not satisfied
        time.sleep(5)