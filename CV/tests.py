from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.test import TestCase
from CV.models import About, Experience, Education, Skills
# Create your tests here.
from CV.views import home_page


class tests(TestCase):
    def test_cv_uses_correct_template(self):
        response = self.client.get('/CV')
        self.assertTemplateUsed(response, 'CV/base.html')

    def test_for_about_model(self):
        about = About.objects.create(description="THis is a test")
        about.save()
        if About.objects.get(pk=1):
            print(About.objects.get(pk=1))
            self.assertIsNotNone(About.objects.get(pk=1))
        else:
            self.fail("Didn't create the about model")

    def test_for_experience_model(self):
        exp = Experience.objects.create(job_description="Testing the exp", job_start_date="2020-06-01",
                                        job_end_date="2020-09-01", job_company="TESTINGG")
        exp.save()
        if Experience.objects.get(pk=1):
            print(Experience.objects.get(pk=1))
            self.assertIsNotNone(Experience.objects.get(pk=1))
            self.assertEqual("Testing the exp", Experience.objects.get(pk=1).job_description)
        else:
            self.fail("Didn't create the experience model")

    def test_for_experience_length_limit(self):
        exp = Experience.objects.create(
            job_title="nRpWUlgun7uFUWEUhsN1xwTdvwCeqqP6e35omB2xQ5z02vGyuG6LfYjXSAwUEP39VKTEamN5u6o60OgTUxzbLYu7WJYieviWbEdqc05Zdg4cjfhKJhzh538MRceQPtPAZcY37hIEl0C6RbtJxZEkwhKeQNzIsarSYyyzYjPr7fzzZoo0NoG23K2tBzfDtaIc8n9dGyRk3siMeFCy1drZUXOFdQhFWJ8obDIvHo5HatmHdcd80fnx4L48fdINnqHyzVTYgzQPTeOOCybNh7X0FxQAwbwYYEgeioY8DLjQMGNrodIyL8Jc5n2eUDgaMRL1Rolr7xehPGRomDEqSb4rcAxyflvI6QBz8GVIVYH5aidn2pSF9jAvkxR8Bv3D33mAHZesSfruXbU3HnThWtdjrZ29RBsXvRrofnIO5iRUnKQCGkBQcTWJikqf8TZKBfnsrpXCohSQH4DY0BCOZCnqeLdwXsQKRfDADJTESmljW8MlyvD3vI3Jm4iEBW98tOLPNUFURmk6ejiCtmgoF6izXNApAcwih68DqyvRqcnc9OQLnQlVcVfrbwp3zJ1oopsN9A7w6hAKOXKNxxDITEm3BShu8ufQaA3zO84SMS52ymliB21EBEuSU7TJB69uwA2mTrAJhgK6I2nThcjH1ZHaTR6peLzUgRYDEW2ENMFIitfOA5ypoAGyFhFn3tuO5wsNmf3vPjDMT488wzOuooQH1894wKL50lSRIvrHv6NrDgiXQrNYSwRvPIQAohhvQcMLDstEYf3GIauM2FQ2ZYhgSXBkQeIpGCsgHvgk2H7A1gzTmpTbUEFxa5EtJwzshkqWB2arjUEjaF8Xn5uqbX63Rih3eJmGxnD6LX2G2Y7vqG8rsNemlPnJnFie3x7hNAwrhJGZWqlevLQb9jrhqwg8kluF7So2ZAGOHUbd5MfWFrHRgTAdE2wbNjcNpBtNAB8lJqKT091kSB0ipP1idA2bPhBk0425xeq8ldsUO8r1",
            job_description="Test",
            job_start_date="2020-06-01", job_end_date="2022-09-01", job_company="Testing")
        exp.save()
        if Experience.objects.get(pk=1):
            print("Should fail")
            self.assertIsNotNone(Experience.objects.get(pk=1))
            self.assertEqual(Experience.objects.get(pk=1).job_title,
                             "nRpWUlgun7uFUWEUhsN1xwTdvwCeqqP6e35omB2xQ5z02vGyuG6LfYjXSAwUEP39VKTEamN5u6o60OgTUxzbLYu7WJYieviWbEdqc05Zdg4cjfhKJhzh538MRceQPtPAZcY37hIEl0C6RbtJxZEkwhKeQNzIsarSYyyzYjPr7fzzZoo0NoG23K2tBzfDtaIc8n9dGyRk3siMeFCy1drZUXOFdQhFWJ8obDIvHo5HatmHdcd80fnx4L48fdINnqHyzVTYgzQPTeOOCybNh7X0FxQAwbwYYEgeioY8DLjQMGNrodIyL8Jc5n2eUDgaMRL1Rolr7xehPGRomDEqSb4rcAxyflvI6QBz8GVIVYH5aidn2pSF9jAvkxR8Bv3D33mAHZesSfruXbU3HnThWtdjrZ29RBsXvRrofnIO5iRUnKQCGkBQcTWJikqf8TZKBfnsrpXCohSQH4DY0BCOZCnqeLdwXsQKRfDADJTESmljW8MlyvD3vI3Jm4iEBW98tOLPNUFURmk6ejiCtmgoF6izXNApAcwih68DqyvRqcnc9OQLnQlVcVfrbwp3zJ1oopsN9A7w6hAKOXKNxxDITEm3BShu8ufQaA3zO84SMS52ymliB21EBEuSU7TJB69uwA2mTrAJhgK6I2nThcjH1ZHaTR6peLzUgRYDEW2ENMFIitfOA5ypoAGyFhFn3tuO5wsNmf3vPjDMT488wzOuooQH1894wKL50lSRIvrHv6NrDgiXQrNYSwRvPIQAohhvQcMLDstEYf3GIauM2FQ2ZYhgSXBkQeIpGCsgHvgk2H7A1gzTmpTbUEFxa5EtJwzshkqWB2arjUEjaF8Xn5uqbX63Rih3eJmGxnD6LX2G2Y7vqG8rsNemlPnJnFie3x7hNAwrhJGZWqlevLQb9jrhqwg8kluF7So2ZAGOHUbd5MfWFrHRgTAdE2wbNjcNpBtNAB8lJqKT091kSB0ipP1idA2bPhBk0425xeq8ldsUO8r1")
        else:
            self.fail("Should fail for now")

    def test_for_education_model(self):
        edu = Education.objects.create(certificate_institute="TEST",
                                       certificate_description="Testing the education",
                                       certificate_start_date="2020-06-01", certificate_end_date="2022-09-01",
                                       certificate_title="TESTING EDUC")
        edu.save()
        if Education.objects.get(pk=1):
            self.assertIsNotNone(Education.objects.get(pk=1))
            self.assertEqual("TESTING EDUC", Education.objects.get(pk=1).certificate_title)
        else:
            self.fail("Didn't create the education model")

    def test_for_education_length_limit(self):
        # Benefits of TDD :)
        edu = Education.objects.create(certificate_institute="TEST",
                                       certificate_description="Testing the education",
                                       certificate_start_date="2020-06-01", certificate_end_date="2022-09-01",
                                       certificate_title="nRpWUlgun7uFUWEUhsN1xwTdvwCeqqP6e35omB2xQ5z02vGyuG6LfYjXSAwUEP39VKTEamN5u6o60OgTUxzbLYu7WJYieviWbEdqc05Zdg4cjfhKJhzh538MRceQPtPAZcY37hIEl0C6RbtJxZEkwhKeQNzIsarSYyyzYjPr7fzzZoo0NoG23K2tBzfDtaIc8n9dGyRk3siMeFCy1drZUXOFdQhFWJ8obDIvHo5HatmHdcd80fnx4L48fdINnqHyzVTYgzQPTeOOCybNh7X0FxQAwbwYYEgeioY8DLjQMGNrodIyL8Jc5n2eUDgaMRL1Rolr7xehPGRomDEqSb4rcAxyflvI6QBz8GVIVYH5aidn2pSF9jAvkxR8Bv3D33mAHZesSfruXbU3HnThWtdjrZ29RBsXvRrofnIO5iRUnKQCGkBQcTWJikqf8TZKBfnsrpXCohSQH4DY0BCOZCnqeLdwXsQKRfDADJTESmljW8MlyvD3vI3Jm4iEBW98tOLPNUFURmk6ejiCtmgoF6izXNApAcwih68DqyvRqcnc9OQLnQlVcVfrbwp3zJ1oopsN9A7w6hAKOXKNxxDITEm3BShu8ufQaA3zO84SMS52ymliB21EBEuSU7TJB69uwA2mTrAJhgK6I2nThcjH1ZHaTR6peLzUgRYDEW2ENMFIitfOA5ypoAGyFhFn3tuO5wsNmf3vPjDMT488wzOuooQH1894wKL50lSRIvrHv6NrDgiXQrNYSwRvPIQAohhvQcMLDstEYf3GIauM2FQ2ZYhgSXBkQeIpGCsgHvgk2H7A1gzTmpTbUEFxa5EtJwzshkqWB2arjUEjaF8Xn5uqbX63Rih3eJmGxnD6LX2G2Y7vqG8rsNemlPnJnFie3x7hNAwrhJGZWqlevLQb9jrhqwg8kluF7So2ZAGOHUbd5MfWFrHRgTAdE2wbNjcNpBtNAB8lJqKT091kSB0ipP1idA2bPhBk0425xeq8ldsUO8r1")
        edu.save()
        if Education.objects.get(pk=1):
            print("Should fail")
            print(Education.objects.get(pk=1).certificate_title)
            self.assertIsNotNone(Education.objects.get(pk=1))
            edu.full_clean()
            self.assertEqual(Education.objects.get(pk=1).certificate_title,
                             "nRpWUlgun7uFUWEUhsN1xwTdvwCeqqP6e35omB2xQ5z02vGyuG6LfYjXSAwUEP39VKTEamN5u6o60OgTUxzbLYu7WJYieviWbEdqc05Zdg4cjfhKJhzh538MRceQPtPAZcY37hIEl0C6RbtJxZEkwhKeQNzIsarSYyyzYjPr7fzzZoo0NoG23K2tBzfDtaIc8n9dGyRk3siMeFCy1drZUXOFdQhFWJ8obDIvHo5HatmHdcd80fnx4L48fdINnqHyzVTYgzQPTeOOCybNh7X0FxQAwbwYYEgeioY8DLjQMGNrodIyL8Jc5n2eUDgaMRL1Rolr7xehPGRomDEqSb4rcAxyflvI6QBz8GVIVYH5aidn2pSF9jAvkxR8Bv3D33mAHZesSfruXbU3HnThWtdjrZ29RBsXvRrofnIO5iRUnKQCGkBQcTWJikqf8TZKBfnsrpXCohSQH4DY0BCOZCnqeLdwXsQKRfDADJTESmljW8MlyvD3vI3Jm4iEBW98tOLPNUFURmk6ejiCtmgoF6izXNApAcwih68DqyvRqcnc9OQLnQlVcVfrbwp3zJ1oopsN9A7w6hAKOXKNxxDITEm3BShu8ufQaA3zO84SMS52ymliB21EBEuSU7TJB69uwA2mTrAJhgK6I2nThcjH1ZHaTR6peLzUgRYDEW2ENMFIitfOA5ypoAGyFhFn3tuO5wsNmf3vPjDMT488wzOuooQH1894wKL50lSRIvrHv6NrDgiXQrNYSwRvPIQAohhvQcMLDstEYf3GIauM2FQ2ZYhgSXBkQeIpGCsgHvgk2H7A1gzTmpTbUEFxa5EtJwzshkqWB2arjUEjaF8Xn5uqbX63Rih3eJmGxnD6LX2G2Y7vqG8rsNemlPnJnFie3x7hNAwrhJGZWqlevLQb9jrhqwg8kluF7So2ZAGOHUbd5MfWFrHRgTAdE2wbNjcNpBtNAB8lJqKT091kSB0ipP1idA2bPhBk0425xeq8ldsUO8r1")
        else:
            self.fail("Should fail for now")

    def test_for_skills_model(self):
        skills = Skills.objects.create(skills_text="Django")
        skills.save()
        if Skills.objects.get(pk=1):
            print(Skills.objects.get(pk=1))
            self.assertIsNotNone(Skills.objects.get(pk=1))
        else:
            self.fail("Didn't create the about model")

    def test_for_interests_model(self):
        interests = Interests.objects.create(skills_text="Django")
        interests.save()
        if Interests.objects.get(pk=1):
            print(Interests.objects.get(pk=1))
            self.assertIsNotNone(Interests.objects.get(pk=1))
        else:
            self.fail("Didn't create the about model")