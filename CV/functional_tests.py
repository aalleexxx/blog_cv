import unittest

from selenium import webdriver


class Tests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    # The user enters the CV section of the webpage
    def test_homepage_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV')
        self.assertIn('CV', self.browser.title)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
