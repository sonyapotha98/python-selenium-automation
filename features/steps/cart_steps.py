from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Open cart page')
def open_cart(context):
    context.app.cart.open_cart()



# @then("Verify 'Your cart is empty' message is shown")
# def verify_cart_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
#     assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


@then('Verify cart is empty')
def verify_cart(context):
    context.app.cart.verify_cart_empty()



# @then('Verify cart has correct product')
# def verify_product_name(context):
#     actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
#     print(f'Actual product in cart name: {actual_name}')
#     assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"
#
#
# @then('Verify cart has {amount} item(s)')
# def verify_cart_items(context, amount):
#     cart_summary = context.driver.find_element(*CART_SUMMARY).text
#     assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"





