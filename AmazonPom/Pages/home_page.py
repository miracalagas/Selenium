from selenium.webdriver.common.by import By
from AmazonPom.base_page.base_page import BasePage


class HomePage(BasePage):

    """search from the search button"""

    search_name = "samsung"
    HOMEPAGE_CONTROL = (By.ID, "anonCarousel1")
    SEARCH_LOCATOR = (By.ID, "twotabsearchtextbox")
    SEARCH_CLICK_BTN = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def search(self):
        """search for word samsung"""
        assert self.wait_for_element(self.HOMEPAGE_CONTROL), True
        self.wait_for_element(self.SEARCH_LOCATOR).send_keys(self.search_name)
        self.wait_for_element(self.SEARCH_CLICK_BTN).click()
