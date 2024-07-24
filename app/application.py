from pages.main_page import MainPage
from pages.base_page import Page
from pages.header import Header
from pages.search_result_page import SearchResultPage


class Application:
    def __init__(self,driver):

        self.base_page = Page(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)

