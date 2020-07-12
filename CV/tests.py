from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from CV.views import home_page


class tests(TestCase):
    def test_fail(self):
        self.fail()

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>CV</title>', html)
        self.assertTrue(html.endswith('</html>'))