from pages.main_page import MainPage
from pages.base_page import Page
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.cart import CartPage
from pages.signin_page import SigninPage


class Application:
    def __init__(self,driver):

        self.base_page = Page(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart = CartPage(driver)
        self.signin_page = SigninPage(driver)


