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
            510,
            delta=5
        )

    def test_style_experience_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        self.browser.set_window_size(1024, 768)
        experience_title = self.browser.find_element_by_id('id_job_title')
        self.assertAlmostEqual(
            experience_title.location['x'] + experience_title.size['width'] / 2,
            465,
            delta=5
        )

    def test_style_education_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/education')
        self.browser.set_window_size(1024, 768)
        education_title = self.browser.find_element_by_id('id_certificate_title')
        self.assertAlmostEqual(
            education_title.location['x'] + education_title.size['width'] / 2,
            465,
            delta=10
        )

    def test_style_skills_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        self.browser.set_window_size(1024, 768)
        skills = self.browser.find_element_by_id('id_skills')
        self.assertAlmostEqual(
            skills.location['x'] + skills.size['width'] / 2,
            370,
            delta=10
        )

    def test_style_interests_page_cv(self):
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        self.browser.set_window_size(1024, 768)
        interests = self.browser.find_element_by_id('id_interest')
        self.assertAlmostEqual(
            interests.location['x'] + interests.size['width'] / 2,
            510,
            delta=5
        )


if __name__ == "__main__":
    unittest.main(warnings='ignore')


class AdminTests(unittest.TestCase):
    # PLEASE READ THE COMMENTS TO ENSURE THE TESTS WORK

    username = 'alex'     # Please replace with the username provided
    password = 'testing'  # Please replace with the password provided

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_edit_about(self):
        self.browser.get('http://127.0.0.1:8000/about')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV')
        edit_about = self.browser.find_element_by_id('Edit')
        self.assertIsNotNone(edit_about)
        edit_about.click()
        test_text = 'TESTING'
        about_text = self.browser.find_element_by_id('id_description')
        about_text.send_keys(test_text)
        save = self.browser.find_element_by_id('Save')
        self.assertIsNotNone(save)
        save.click()
        self.assertNotEqual(about_text, self.browser.find_element_by_id('id_about'))
        self.browser.get('http://127.0.0.1:8000/CV')
        updated_text = self.browser.find_element_by_id('id_about')
        # PLEASE PROVIDE THE PREVIOUS DATA FROM THE DATABASE
        previous_entry = 'A'
        test_text = previous_entry + test_text
        self.assertEqual(test_text, updated_text.text)
        self.assertEqual(test_text, updated_text.text)

    def test_create_interests(self):
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        create_interest = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_interest)
        create_interest.click()
        test_text = 'T6'
        time.sleep(15)
        interests_text = self.browser.find_element_by_id('id_interests_text')
        interests_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        time.sleep(3)
        save.click()
        time.sleep(3)
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id(
            'id_interests8')
        self.assertEqual(test_text, updated_text.text)

    def test_edit_interests(self):
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        # Put the correct number for the element you want to test bellow
        edit_interest = self.browser.find_element_by_id('id_edit7')
        self.assertIsNotNone(edit_interest)
        edit_interest.click()
        test_text = 'TESTING'
        interest_text = self.browser.find_element_by_id('id_interests_text')
        interest_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        # PLEASE PROVIDE THE PREVIOUS DATA FROM THE DATABASE
        previous_entry = 'T6'
        test_text = previous_entry + test_text
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id('id_interests7')
        self.assertEqual(test_text, updated_text.text)

    def test_delete_interests(self):
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/interests')
        time.sleep(10)
        # Put the correct number for the element you want to test bellow
        delete_interest = self.browser.find_element_by_id(
            'id_delete8')
        self.assertIsNotNone(delete_interest)
        delete_interest.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            # Put the correct number for the element you want to test bellow
            self.browser.find_element_by_id('id_delete6')
            self.fail("Found the Element")
        except:
            pass

    def test_create_experience(self):
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        create_experience = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_experience)
        create_experience.click()
        test_text = 'TESTING CREATE'
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
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id(
            'id_job_title12')
        self.assertEqual(test_text, updated_text.text)

    def test_edit_experience(self):
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        # Put the correct number for the element you want to test bellow
        edit_experience = self.browser.find_element_by_id(
            'id_edit2')
        self.assertIsNotNone(edit_experience)
        edit_experience.click()
        time.sleep(3)
        test_text = 'TESTING'
        experience_description = self.browser.find_element_by_id('id_job_description')
        experience_description.send_keys(test_text)
        experience_job_title = self.browser.find_element_by_id('id_job_title')
        experience_job_title.send_keys(test_text + " Title")
        experience_job_company = self.browser.find_element_by_id('id_job_company')
        experience_job_company.send_keys("Test")
        time.sleep(3)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        time.sleep(5)
        # PLEASE PROVIDE THE PREVIOUS DATA FROM THE DATABASE
        previous_entry = 'T'
        test_text = previous_entry + test_text
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id('id_job_title2')
        self.assertEqual(test_text + ' TITLE', updated_text.text)

    def test_delete_experience(self):
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/experience')
        time.sleep(10)
        # Put the correct number for the element you want to test bellow
        delete_experience = self.browser.find_element_by_id(
            'id_delete12')
        self.assertIsNotNone(delete_experience)
        delete_experience.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            # Put the correct number for the element you want to test bellow
            self.browser.find_element_by_id('id_delete12')
            self.fail("Found the Element")
        except:
            pass

    def test_create_education(self):
        self.browser.get('http://127.0.0.1:8000/CV/education')
        time.sleep(10)
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/education')
        time.sleep(10)
        create_education = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_education)
        create_education.click()
        test_text = 'TESTING CREATE'
        time.sleep(3)
        education_description = self.browser.find_element_by_id('id_certificate_description')
        education_description.send_keys(test_text)
        education_title = self.browser.find_element_by_id('id_certificate_title')
        education_title.send_keys(test_text)
        education_company = self.browser.find_element_by_id('id_certificate_institute')
        education_company.send_keys(test_text)
        time.sleep(3)
        education_start_date = self.browser.find_element_by_id('id_certificate_start_date')
        education_start_date.send_keys("2018-09-01")
        education_end_date = self.browser.find_element_by_id('id_certificate_end_date')
        education_end_date.send_keys("2021-06-01")
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        time.sleep(3)
        save.click()
        time.sleep(3)
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id(
            'id_certificate_title9')
        self.assertEqual(test_text, updated_text.text)

    def test_edit_education(self):
        self.browser.get('http://127.0.0.1:8000/CV/education')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/education')
        # Put the correct number for the element you want to test bellow
        edit_education = self.browser.find_element_by_id(
            'id_edit1')
        self.assertIsNotNone(edit_education)
        edit_education.click()
        time.sleep(3)
        test_text = 'TESTING'
        education_description = self.browser.find_element_by_id('id_certificate_description')
        education_description.send_keys(test_text)
        education_certification_title = self.browser.find_element_by_id('id_certificate_title')
        education_certification_title.send_keys(test_text + " Title")
        education_certification_institute = self.browser.find_element_by_id('id_certificate_institute')
        education_certification_institute.send_keys("Test")
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        time.sleep(3)
        # PLEASE PROVIDE THE PREVIOUS DATA FROM THE DATABASE
        previous_entry = 'A'
        test_text = previous_entry + test_text
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id('id_certificate_title1')
        self.assertEqual(test_text + " TITLE", updated_text.text)

    def test_delete_education(self):
        self.browser.get('http://127.0.0.1:8000/CV/education')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/education')
        time.sleep(10)
        # Put the correct number for the element you want to test bellow
        delete_education = self.browser.find_element_by_id(
            'id_delete9')
        self.assertIsNotNone(delete_education)
        delete_education.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            # Put the correct number for the element you want to test bellow
            self.browser.find_element_by_id('id_delete9')
            self.fail("Found the Element")
        except:
            pass

    def test_create_skills(self):
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        create_skills = self.browser.find_element_by_id('id_create')
        self.assertIsNotNone(create_skills)
        create_skills.click()
        test_text = 'TESTING CREATE'
        skills_text = self.browser.find_element_by_id('id_skills_text')
        skills_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        time.sleep(3)
        save.click()
        time.sleep(5)
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id(
            'id_skills15')
        self.assertEqual(test_text, updated_text.text)

    def test_edit_skills(self):
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        # Put the correct number for the element you want to test bellow
        edit_skills = self.browser.find_element_by_id(
            'id_edit7')
        self.assertIsNotNone(edit_skills)
        edit_skills.click()
        test_text = 'TESTING'
        skills_text = self.browser.find_element_by_id('id_skills_text')
        skills_text.send_keys(test_text)
        save = self.browser.find_element_by_id('id_save')
        self.assertIsNotNone(save)
        save.click()
        # Put the correct number for the element you want to test bellow
        updated_text = self.browser.find_element_by_id('id_skills7')
        # PLEASE PROVIDE THE PREVIOUS DATA FROM THE DATABASE
        previous_entry = 'Test'
        test_text = previous_entry + test_text
        self.assertEqual(test_text, updated_text.text)
        self.assertEqual(test_text, updated_text.text)

    def test_delete_skills(self):
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        username.send_keys(username)
        password.send_keys(password)

        self.browser.find_element_by_id("Login").click()
        time.sleep(3)
        self.browser.get('http://127.0.0.1:8000/CV/skills')
        time.sleep(10)
        # Put the correct number for the element you want to test bellow
        delete_skills = self.browser.find_element_by_id(
            'id_delete15')
        self.assertIsNotNone(delete_skills)
        delete_skills.click()
        confirm = self.browser.find_element_by_id('id_confirm')
        confirm.click()
        try:
            # Put the correct number for the element you want to test bellow
            self.browser.find_element_by_id('id_delete15')
            self.fail("Found the Element")
        except:
            pass
