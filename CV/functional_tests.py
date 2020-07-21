import unittest

from selenium import webdriver
import time


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


class AdminTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_edit_about(self):
        self.browser.get('http://127.0.0.1:8000/about/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/about/')
        edit_about = self.browser.find_element_by_id('Edit')
        self.assertIsNotNone(edit_about)
        edit_about.click()
        test_text = 'Testing'
        about_text = self.browser.find_element_by_id('id_about')
        about_text.send_keys(test_text)
        save = self.browser.find_element_by_id('Save')
        self.assertIsNotNone(save)
        save.click()
        self.assertNotEqual(about_text, self.browser.find_element_by_id('id_text'))
        self.browser.get('http://127.0.0.1:8000/about/')
        updated_text = self.browser.find_element_by_id('id_text')
        self.assertEqual(test_text, updated_text.text)
        self.assertEqual(test_text, updated_text.text)

    def test_edit_interests(self):
        self.browser.get('http://127.0.0.1:8000/interests/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/interests/')
        edit_interest = self.browser.find_element_by_id('id_edit')
        self.assertIsNotNone(edit_interest)
        edit_interest.click()
        test_text = 'Testing'
        interest_text = self.browser.find_element_by_id('id_interests')
        interest_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        updated_text = self.browser.find_element_by_id('id_interests')
        self.assertEqual(test_text, updated_text.text)

    def test_create_interests(self):
        self.browser.get('http://127.0.0.1:8000/interests/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/interests/')
        create_interest = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_interest)
        create_interest.click()
        test_text = 'Testing Create '
        time.sleep(15)
        interests_text = self.browser.find_element_by_id('id_interests')
        interests_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        time.sleep(3)
        save.click()
        time.sleep(3)
        updated_text = self.browser.find_element_by_id(
            'id_interests')
        self.assertEqual(test_text, updated_text.text)

    def test_delete_interests(self):
        self.browser.get('http://127.0.0.1:8000/interests/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/interests/')
        time.sleep(10)
        delete_interest = self.browser.find_element_by_id(
            'id_delete')
        self.assertIsNotNone(delete_interest)
        delete_interest.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            self.browser.find_element_by_id('id_delete')
        except:
            pass

    def test_edit_experience(self):
        self.browser.get('http://127.0.0.1:8000/experience/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/experience/')
        edit_experience = self.browser.find_element_by_id(
            'id_edit')
        self.assertIsNotNone(edit_experience)
        edit_experience.click()
        time.sleep(3)
        test_text = 'Testing'
        experience_description = self.browser.find_element_by_id('id_job_description')
        experience_description.send_keys(test_text)
        experience_job_title = self.browser.find_element_by_id('id_job_title')
        experience_job_title.send_keys(test_text + " Title")
        experience_job_company = self.browser.find_element_by_id('id_job_company')
        experience_job_company.send_keys("Test")
        experience_start_date = self.browser.find_element_by_id('id_job_start_date')
        time.sleep(3)
        experience_start_date.send_keys("2020-06-01")
        experience_end_date = self.browser.find_element_by_id('id_job_end_date')
        experience_end_date.send_keys('2020-09-06')
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        time.sleep(50)
        updated_text = self.browser.find_element_by_id('id_job_title')
        self.assertEqual(test_text + " Title", updated_text.text)

    def test_create_experience(self):
        self.browser.get('http://127.0.0.1:8000/experience/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/experience/')
        create_experience = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_experience)
        create_experience.click()
        test_text = 'Testing Create'
        time.sleep(3)
        experience_text = self.browser.find_element_by_id('id_job_description')
        experience_text.send_keys(test_text)
        experience_title = self.browser.find_element_by_id('id_job_title')
        experience_title.send_keys(test_text)
        experience_company = self.browser.find_element_by_id('id_job_company')
        experience_company.send_keys(test_text)
        time.sleep(3)
        experience_start_date = self.browser.find_element_by_id('id_job_start_date')
        experience_start_date.send_keys("2020-06-01")
        experience_end_date = self.browser.find_element_by_id('id_job_end_date')
        experience_end_date.send_keys("2020-09-06")
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        time.sleep(3)
        save.click()
        time.sleep(3)
        updated_text = self.browser.find_element_by_id(
            'id_job_title')
        self.assertEqual(test_text, updated_text.text)

    def test_delete_experience(self):
        self.browser.get('http://127.0.0.1:8000/experience/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/experience/')
        time.sleep(10)
        delete_experience = self.browser.find_element_by_id(
            'id_delete')
        self.assertIsNotNone(delete_experience)
        delete_experience.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            self.browser.find_element_by_id('id_delete')
        except:
            pass

    def test_create_education(self):
        self.browser.get('http://127.0.0.1:8000/education/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/education/')
        create_education = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_education)
        create_education.click()
        test_text = 'Testing Create'
        time.sleep(20)
        education_description = self.browser.find_element_by_id('id_certificate_description')
        education_description.send_keys(test_text)
        education_title = self.browser.find_element_by_id('id_certificate_title')
        education_title.send_keys(test_text)
        education_company = self.browser.find_element_by_id('id_certificate_institute')
        education_company.send_keys(test_text)
        time.sleep(10)
        education_start_date = self.browser.find_element_by_id('id_certificate_start_date')
        education_start_date.send_keys("2018-09-01")
        education_end_date = self.browser.find_element_by_id('id_certificate_end_date')
        education_end_date.send_keys("2021-06-01")
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        time.sleep(3)
        save.click()
        time.sleep(3)
        updated_text = self.browser.find_element_by_id(
            'id_certificate_title')
        self.assertEqual(test_text, updated_text.text)

    def test_edit_education(self):
        self.browser.get('http://127.0.0.1:8000/education/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/education/')
        edit_education = self.browser.find_element_by_id(
            'id_edit')
        self.assertIsNotNone(edit_education)
        edit_education.click()
        time.sleep(3)
        test_text = 'Testing'
        education_description = self.browser.find_element_by_id('id_certificate_description')
        education_description.send_keys(test_text)
        education_certification_title = self.browser.find_element_by_id('id_certificate_title')
        education_certification_title.send_keys(test_text + " Title")
        education_certification_institutue = self.browser.find_element_by_id('id_certificate_institute')
        education_certification_institutue.send_keys("Test")
        education_start_date = self.browser.find_element_by_id('id_certificate_start_date')
        education_start_date.send_keys("2020-06-01")
        education_end_date = self.browser.find_element_by_id('id_certificate_end_date')
        education_end_date.send_keys('2020-09-06')
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        time.sleep(3)
        updated_text = self.browser.find_element_by_id('id_certificate_title')
        self.assertEqual(test_text + " Title", updated_text.text)

    def test_delete_education(self):
        self.browser.get('http://127.0.0.1:8000/education/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/education/')
        time.sleep(10)
        delete_education = self.browser.find_element_by_id(
            'id_delete')
        self.assertIsNotNone(delete_education)
        delete_education.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            self.browser.find_element_by_id('id_delete')
            self.fail("Found the Element")
        except:
            pass

    def test_create_skills(self):
        self.browser.get('http://127.0.0.1:8000/skills/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/skills/')
        create_skills = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_skills)
        create_skills.click()
        test_text = 'Testing Create '
        skills_text = self.browser.find_element_by_id('id_skills')
        skills_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        time.sleep(3)
        save.click()
        time.sleep(3)
        updated_text = self.browser.find_element_by_id(
            'id_text')
        self.assertEqual(test_text, updated_text.text)

    def test_delete_skills(self):
        self.browser.get('http://127.0.0.1:8000/skills/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/skills/')
        time.sleep(10)
        delete_skills = self.browser.find_element_by_id(
            'id_delete')
        self.assertIsNotNone(delete_skills)
        delete_skills.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            self.browser.find_element_by_id('id_delete')
        except:
            pass

    def test_edit_skills(self):
        self.browser.get('http://127.0.0.1:8000/skills/')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys('alex')
        password.send_keys('testing')

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/skills/')
        edit_skills = self.browser.find_element_by_id(
            'id_edit')
        self.assertIsNotNone(edit_skills)
        edit_skills.click()
        test_text = 'Testing'
        skills_text = self.browser.find_element_by_id('id_skills')
        skills_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        updated_text = self.browser.find_element_by_id('id_text')
        self.assertEqual(test_text, updated_text.text)
        self.assertEqual(test_text, updated_text.text)
