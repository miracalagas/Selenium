from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def wait_for_element(self, locator):

        return self.wait.until(ec.element_to_be_clickable(locator))

    def wait_for_elements(self, locator):

        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def hover(self, locator):

        hover_element = self.wait_for_element(locator)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()