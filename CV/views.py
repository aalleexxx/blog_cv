# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from CV.models import About, Education


class AboutView(ListView):
    model = About

    def get_queryset(self):
        return About.objects.all()

class EducationView(ListView):
    model = Education

    def get_queryset(self):
        return Education.objects.all()
