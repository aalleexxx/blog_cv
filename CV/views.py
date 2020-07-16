# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from CV.models import About, Education, Experience, Skills, Interests


class AboutView(ListView):
    model = About

    def get_queryset(self):
        return About.objects.all()


class EducationView(ListView):
    model = Education

    def get_queryset(self):
        return Education.objects.all()


class ExperienceView(ListView):
    model = Experience

    def get_queryset(self):
        return Experience.objects.all()


class SkillsView(ListView):
    model = Skills

    def get_queryset(self):
        return Skills.objects.all()


class InterestsView(ListView):
    model = Interests

    def get_queryset(self):
        return Interests.objects.all()
