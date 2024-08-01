from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR,'a[data-test="@web/CartLink"]')
    SIGNIN_BTN = (By.XPATH, "//*[@data-test='@web/AccountLink']")
    NAV_SIGNIN_BTN = (By.XPATH, "//*[@data-test='accountNav-signIn']")

    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)

    def click_signin(self):
        self.click(*self.SIGNIN_BTN)

    def click_nav_signin(self):
        self.click(*self.NAV_SIGNIN_BTN)



