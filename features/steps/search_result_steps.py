from selenium.webdriver.common.by import By
from behave import then,when,given
from time import sleep


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product} not in {url}'


@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'


@when('Add {product} to cart')
def add_to_cart(context,product):
    context.driver.find_element(By.CSS_SELECTOR, '[id*="addToCartButton"]').click()
    sleep(5)


@when('Save the expected product name')
def expected_product(context):
    context.expected_item = context.driver.find_elements(By.XPATH, '//a[@data-test="product-title"]')[0].text


@when('From right side navigation menu, click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="shippingButton"]').click()
    sleep(5)



@then('Verify Added to cart text is shown')
def verify_add_to_cart_text(context):
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.XPATH,'//span[text()="Added to cart"]').text
    assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'


@then('Verify cart has the product')
def verify_product_in_cart(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '[data-test="cartItem-title"]').text
    print(actual_text)
    print(context.expected_item)
    assert context.expected_item in actual_text, f'Expected {context.expected_item} not in actual {actual_text}'











