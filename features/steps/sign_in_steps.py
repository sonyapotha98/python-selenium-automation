from selenium.webdriver.common.by import By
from behave import then


@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.signin_page.verify_signin_opened()