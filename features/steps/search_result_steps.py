from selenium.webdriver.common.by import By
from behave import then,when
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)


@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    context.app.search_results_page.verify_product_in_url(expected_product)


@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'


@when('Add {product} to cart')
def add_to_cart(context,product):
    context.app.search_result_page.add_to_cart()
# @when('Click on Add to Cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
#     # context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click()
#     context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))


@when('Save the expected product name')
def save_product_name(context):
    context.app.cart.save_product_name()


# @when('Store product name')
# def store_product_name(context):
#     context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
#     print(f'Product stored: {context.product_name}')


@when('From right side navigation menu, click add to cart')
def nav_add_to_cart(context):
    context.app.search_result_page.nav_add_to_cart()

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
    context.app.cart.verify_product_in_cart()











