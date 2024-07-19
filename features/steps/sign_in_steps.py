from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")