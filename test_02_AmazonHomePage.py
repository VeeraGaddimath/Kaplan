from config.Settings import *
from Test_Page.Amazon_HomePage_Locators import *
def test_allmenu(setup):
    driver = setup
    driver.find_element(By.XPATH, HOMEPAGE.ALLMENU_BTN).click()
def test_seeall(setup):
    driver = setup
    shop_by_category = driver.find_element(By.XPATH, HOMEPAGE.SEEALL_BTN)
    driver.implicitly_wait(5)
    driver.execute_script("arguments[0].scrollIntoView();", shop_by_category)
    time.sleep(3)
    shop_by_category.click()
def test_car_motorbike_industrial(setup):
    driver = setup
    driver.execute_script("window.scrollBy(0, 1000)")
    car_motorbike_industrial = driver.find_element(By.XPATH, HOMEPAGE.CAR_MOTORBIKE_INDUSTRY_BTN)
    driver.implicitly_wait(5)
    time.sleep(3)
    car_motorbike_industrial.click()
def test_car_accessories(setup):
    driver = setup
    car_accessories = driver.find_element(By.XPATH, HOMEPAGE.CAR_ACCESSARIES_BTN)
    driver.implicitly_wait(5)
    time.sleep(3)
    car_accessories.click()
def test_click_radio_button(setup):
    driver = setup
    driver.implicitly_wait(5)
    radio_btn = driver.find_element(By.XPATH, HOMEPAGE.RADIO_BTN)
    driver.execute_script("arguments[0].scrollIntoView();", radio_btn)
    radio_btn.click()
def test_verify_pricess(setup):
    driver = setup
    product_prices = driver.find_elements(By.XPATH, HOMEPAGE.VERIFY_PRICE)
    for price in product_prices:
        assert int(price.text.replace(',', '')) < 500