from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, '//div[@data-test="boxEmptyMsg"]')
    PRODUCT_IN_CART = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')
    SIDE_NAV_PRODUCT_NME = (By.CSS_SELECTOR,"[data-test='content-wrapper'] h4")

    def open_cart(self):
        self.open_url('https://www.target.com/cart')
        sleep(5)

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def save_product_name(self):
        self.product_name = self.find_text(*self.SIDE_NAV_PRODUCT_NME)
        print("Actual product: " + self.product_name)
        sleep(4)

    def verify_product_in_cart(self):
        product_in_cart_name = self.find_text(*self.PRODUCT_IN_CART)
        print(product_in_cart_name)
        print(self.product_name)
        assert self.product_name in product_in_cart_name, f'Expected: {self.product_name} not in actual : {product_in_cart_name}'