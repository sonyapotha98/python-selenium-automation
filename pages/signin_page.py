from pages.base_page import Page
from selenium.webdriver.common.by import By


class SigninPage(Page):
    SIGN_IN_TXT = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_signin_opened(self):
        self.find_element(*self.SIGN_IN_TXT)


