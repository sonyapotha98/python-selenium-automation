from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_product(context):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)


@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'


@when('Click cart to view')
def select_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'a[data-test="@web/CartLink"]').click()


@then('Verify cart is empty')
def verify_cart(context):
    expected_text = "Your cart is empty"
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()
    sleep(5)
    actual_text = context.driver.find_element(By.XPATH, '//div[@data-test="boxEmptyMsg"]').text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'


@when('Click Sign In')
def sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    sleep(2)


@when('From right side navigation menu, click Sign In')
def nav_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(2)


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")



