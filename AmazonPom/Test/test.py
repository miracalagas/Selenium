

from selenium import webdriver
from AmazonPom.Pages.login_page import LoginPage
from AmazonPom.Pages.home_page import HomePage
from AmazonPom.Pages.category_page import CategoryPage
from AmazonPom.Pages.product_page import ProductPage
from AmazonPom.Pages.wishlist import Wishlist
import unittest


class TestAmazon(unittest.TestCase):
    """Test case is:
    1. Go to website
    2. Click login page button
    3. Try to logged in
    4. Search "samsung" on site
    5. Search third product result of search
    6. Add product to wishlist
    7. Go to wishlist
    8. Delete items from wishlist
    9. Tear down
    """

    @classmethod
    def setUpClass(self):

        self.website = "https://www.amazon.com/"
        self.driver = webdriver.Chrome("C:/Users/mirac.alagas/Desktop/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.LoginPage = LoginPage(self.driver)
        self.HomePage = HomePage(self.driver)
        self.CategoryPage = CategoryPage(self.driver)
        self.ProductPage = ProductPage(self.driver)
        self.Wishlist = Wishlist(self.driver)

    def test_amazon(self):

        self.LoginPage.login()
        self.HomePage.search()
        self.CategoryPage.next_page()
        self.CategoryPage.select_third_product()
        self.ProductPage.add_to_list()
        self.Wishlist.delete_wishlist()

    @classmethod
    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

