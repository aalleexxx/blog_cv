from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='CV'),
    path('education', views.EducationView.as_view(), name='Education'),
    path('experience', views.ExperienceView.as_view(), name='Experience'),
    path('skills', views.SkillsView.as_view(), name='Skills'),
    path('interests', views.InterestsView.as_view(), name='Interests'),
]
