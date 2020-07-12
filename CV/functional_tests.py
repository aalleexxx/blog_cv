import unittest

from selenium import webdriver


class Tests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_first(self):
        self.fail("First test")


if __name__ == "__main__":
    unittest.main(warnings='ignore')
