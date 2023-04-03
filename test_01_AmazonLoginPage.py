from config.Settings import *
from Test_Page.Amazon_Loginpage_Locators import *
from TestData.testData import *
def test_login(setup):
    driver = setup
    # Click on the SignIn button on the Amazon homepage
    driver.find_element(By.XPATH,LOGINPAGE.account).click()

    # Enter email and click Continue
    email_field = driver.find_element(By.XPATH, LOGINPAGE.username)
    email_field.clear()
    email_field.send_keys(userdata.username)
    continue_button = driver.find_element(By.XPATH, LOGINPAGE.continue_btn)
    continue_button.click()

    # Enter password and click Sign In
    pwd_field = driver.find_element(By.XPATH, LOGINPAGE.password)
    pwd_field.clear()
    pwd_field.send_keys(userdata.user_pwd)
    signin_button = driver.find_element(By.XPATH, LOGINPAGE.signin_btn)
    signin_button.click()

    # Verify login
    assert "Amazon Sign In" in driver.title
