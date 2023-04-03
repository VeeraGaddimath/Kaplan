from config.Settings import *
from Test_Page.Amazon_CartPage_Locators import *

def test_add_to_cart(setup):
    driver=setup
    global products
    products = []
    product_names = driver.find_elements(By.XPATH , ADD_TO_CART.PRODUCT_NAME)
    product_prices = driver.find_elements(By.XPATH , ADD_TO_CART.PRODUCT_PRICE)
    for i in range(4):
        product = {}
        product['name'] = product_names[i].text
        product['price'] = product_prices[i].text
        products.append(product)

    print(products)

    # Add all the 4 the items to the cart
    for i in range(4):
        # Click on the product name to go to the product page
        current_window = driver.current_window_handle
        product_names[i].click()
        window_handles = driver.window_handles
        for handle in window_handles:
            if handle != current_window:
                new_window = handle
                break
        driver.switch_to.window(new_window)

        # Add the product to the cart
        wait = WebDriverWait(driver, 10)
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.XPATH, ADD_TO_CART.ADD_TO_CART_BTN)))
        # Click the element
        driver.implicitly_wait(5)
        add_to_cart_button.click()
        # Close the new window or tab
        driver.close()

        # Switch back to the original window or tab
        driver.switch_to.window(current_window)
    driver.refresh()
    time.sleep(5)
    driver.execute_script('window.scrollBy(0, -500);')

    driver.find_element(By.XPATH, ADD_TO_CART.LOCAL_BTN).click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, ADD_TO_CART.PROCEED_TO_CHECKOUT_BTN).click()
    driver.implicitly_wait(5)

def test_select_address(setup):
    driver=setup
    driver.implicitly_wait(5)
    address = driver.find_element(By.XPATH, ADDRESS.DEFAULT_ADDRESS)
    driver.implicitly_wait(5)
    if address.is_enabled():
        print("address is selected")
    else:
        address.click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, ADDRESS.MANUAL_ADDRESS).click()
    time.sleep(5)

def test_validate_prices_in_payment_page(setup):
    driver=setup
    # validate the prices of the items in the payment page matches
    product_in_payment = driver.find_elements(By.CSS_SELECTOR, PRODUCTPAYMENT.PRODUCT_IN_PAYMENT)
    for product_names, product_prices in products:
        for item in product_in_payment:
            if product_names in item.text:
                assert product_prices in item.text, f"Price doesn't match for {product_names}"