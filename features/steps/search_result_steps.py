from selenium.webdriver.common.by import By
from behave import then,when
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


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
# @when('Click on Add to Cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
#     # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
#     context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))

@when('Save the expected product name')
def expected_product(context):
    context.expected_item = context.driver.wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, '//a[@data-test="product-title"]')))[0].text

# @when('Store product name')
# def store_product_name(context):
#     context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
#     print(f'Product stored: {context.product_name}')


@when('From right side navigation menu, click add to cart')
def click_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shippingButton"]'))).click()
    sleep(5)

# @when('Confirm Add to Cart button from side navigation')
# def side_nav_click_add_to_cart(context):
#     context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
#     sleep(6)


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











