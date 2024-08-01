from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
    NAV_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*= 'addToCart']")
    SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULT_TEXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def add_to_cart(self):
        self.wait_and_click(*self.ADD_TO_CART_BTN)


    def nav_add_to_cart(self):
        self.wait_and_click(*self.NAV_ADD_TO_CART)
        sleep(6)

