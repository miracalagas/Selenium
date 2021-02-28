from selenium.webdriver.common.by import By
from AmazonPom.base_page.base_page import BasePage


class CategoryPage(BasePage):
    NEXT_PAGE = (By.CSS_SELECTOR, "[class='a-last']")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height")
    IS_PAGE_TWO = (By.CSS_SELECTOR, ".a-section.a-spacing-small.a-spacing-top-small")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def next_page(self):
        self.wait_for_element(self.NEXT_PAGE).click()
        #a = self.wait_for_element(self.IS_PAGE_TWO).text
        #assert "17-32" in a

    def select_third_product(self):
        self.wait_for_elements(self.PRODUCT_PAGE)[2].click()

