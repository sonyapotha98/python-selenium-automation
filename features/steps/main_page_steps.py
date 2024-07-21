from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()


@when('Click Sign In')
def sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-test='@web/AccountLink']"))).click()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search()


@when('From right side navigation menu, click Sign In')
def nav_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-test='accountNav-signIn']"))).click()
    sleep(2)


# @when('Click on Cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
@when('Click cart to view')
def select_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'a[data-test="@web/CartLink"]').click()


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")


@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)  # convert str "6" ==> to int 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'

    # Make sure to always assert len() for multiple elements as shown above
    # because .find_elements() function never fails.
    # This code with incorrect locator will always pass:
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")