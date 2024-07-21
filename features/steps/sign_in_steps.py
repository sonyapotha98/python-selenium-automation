from selenium.webdriver.common.by import By
from behave import then


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")