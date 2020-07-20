import unittest

from selenium import webdriver


class UserTests(unittest.TestCase):

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

    def test_skills_page_cv(self):
        # The user opens the browser and goes to the skills section of the website
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        # The user checks the title of the website
        self.assertIn('CV', self.browser.title)
        # The user looks for the skills text
        self.assertIsNotNone(self.browser.find_element_by_id("id_skills"))

    def test_interests_page_cv(self):
        # The user opens the browser and goes to the interests section of the website
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        # The user checks the title of the website
        self.assertIn('CV', self.browser.title)
        # The user looks for the interests content
        self.assertIsNotNone(self.browser.find_element_by_id("id_interest"))

    def test_style_homepage_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV')
        self.browser.set_window_size(1024, 768)
        about_text = self.browser.find_element_by_id('id_about')
        self.assertAlmostEqual(
            about_text.location['x'] + about_text.size['width'] / 2,
            630,
            delta=5
        )

    def test_style_experience_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        self.browser.set_window_size(1024, 768)
        experience_title = self.browser.find_element_by_id('id_job_title')
        self.assertAlmostEqual(
            experience_title.location['x'] + experience_title.size['width'] / 2,
            580,
            delta=5
        )

    def test_style_education_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/education')
        self.browser.set_window_size(1024, 768)
        education_title = self.browser.find_element_by_id('id_certificate_title')
        self.assertAlmostEqual(
            education_title.location['x'] + education_title.size['width'] / 2,
            580,
            delta=10
        )

    def test_style_skills_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        self.browser.set_window_size(1024, 768)
        skills = self.browser.find_element_by_id('id_skills')
        self.assertAlmostEqual(
            skills.location['x'] + skills.size['width'] / 2,
            360,
            delta=10
        )

    def test_style_interests_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        self.browser.set_window_size(1024, 768)
        interests = self.browser.find_element_by_id('id_interest')
        self.assertAlmostEqual(
            interests.location['x'] + interests.size['width'] / 2,
            630,
            delta=5
        )


if __name__ == "__main__":
    unittest.main(warnings='ignore')
