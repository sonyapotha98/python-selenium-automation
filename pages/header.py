from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search(self):
        self.input_text('coffee',*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        #wait for the search result to laod
        sleep(5)

