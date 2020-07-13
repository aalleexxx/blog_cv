from django.http import HttpRequest
from django.test import TestCase
from CV.models import About
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
            self.assertIsNotNone(About.objects.get(pk=1))
        else:
            self.fail("Didn't create the object")



