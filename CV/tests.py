from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from CV.views import home_page


class tests(TestCase):
    def test_cv_uses_correct_template(self):
        response = self.client.get('/CV')
        self.assertTemplateUsed(response, 'CV/base.html')

