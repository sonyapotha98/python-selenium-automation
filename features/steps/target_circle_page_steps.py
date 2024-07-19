from selenium.webdriver.common.by import By
from behave import given,then


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify page has {number} benefit cells')
def verify_no_of_benefit_cells(context,number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR,'div.cell-item-content')
    assert len(links) == number , f'expected {number} links but got only {len(links)}'



