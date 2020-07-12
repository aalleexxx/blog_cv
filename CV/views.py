from django.http import HttpResponse

# Create your views here.
from django.template.context_processors import request


def home_page(request):
    return HttpResponse('<html><title>CV</title></html>')