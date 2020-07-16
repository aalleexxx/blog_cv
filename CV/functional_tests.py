import unittest

from selenium import webdriver


class Tests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_homepage_cv(self):
        # The user opens the browser and goes to the CV application website
        self.browser.get('http://127.0.0.1:8000/CV')
        # The user checks the title of the website
        self.assertIn('CV', self.browser.title)
        # The user looks for the about text
        self.assertIsNotNone(self.browser.find_element_by_id("id_about"))

    def test_education_page_cv(self):
        # The user opens the browser and goes to the education part of the website
        self.browser.get('http://127.0.0.1:8000/CV/education')
        # The user checks the title of the website
        self.assertIn('CV', self.browser.title)
        # The user looks for the content of the education section
        self.assertIsNotNone(self.browser.find_element_by_id("id_certificate_title"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_certificate_description"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_certificate_institute"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_certificate_start_date"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_certificate_end_date"))

    def test_experience_page_cv(self):
        # The user opens the browser and goes to the experience section of the website
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        # The user checks the title of the website
        self.assertIn('CV', self.browser.title)
        # The user looks for the content of the experience section
        self.assertIsNotNone(self.browser.find_element_by_id("id_job_title"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_job_description"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_job_company"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_job_start_date"))
        self.assertIsNotNone(self.browser.find_element_by_id("id_job_end_date"))



if __name__ == "__main__":
    unittest.main(warnings='ignore')
