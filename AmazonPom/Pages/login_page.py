from selenium.webdriver.common.by import By
from AmazonPom.base_page.base_page import BasePage


class LoginPage (BasePage):

    Mail = "miracalagas1@gmail.com"
    password = "mirac1234"

    LOGIN_BTN = (By.ID, "nav-link-accountList-nav-line-1")
    EMAIL_LOCATOR = (By.ID, "ap_email")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    PASSWRD_LOCATOR = (By.ID,"ap_password")
    SIGN_BTN = (By.ID, "signInSubmit")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def login(self):
        self.wait_for_element(self.LOGIN_BTN).click()
        self.wait_for_element(self.EMAIL_LOCATOR).send_keys(self.Mail)
        self.wait_for_elements(self.CONTINUE_BTN)[1].click()
        self.wait_for_element(self.PASSWRD_LOCATOR).send_keys(self.password)
        self.wait_for_element(self.SIGN_BTN).click()
