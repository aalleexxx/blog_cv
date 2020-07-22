from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='CV'),
    path('', views.AboutView.as_view(), name='about'),
    path('/update/<int:pk>', views.AboutUpdateView.as_view(), name='about_edit'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('skills/update/<int:pk>', views.SkillsUpdateView.as_view(), name='skills_edit'),
    path('skills/create/', views.SkillsCreateView.as_view(), name='skills_create'),
    path('skills/delete/<int:pk>', views.SkillsDeleteView.as_view(), name='skills_delete'),
    path('interests/', views.InterestsView.as_view(), name='interests'),
    path('interests/update/<int:pk>', views.InterestsUpdateView.as_view(), name='interests_edit'),
    path('interests/create/', views.InterestsCreateView.as_view(), name='interests_create'),
    path('interests/delete/<int:pk>', views.InterestsDeleteView.as_view(), name='interests_delete'),
    path('experience/', views.ExperienceView.as_view(), name='experience'),
    path('experience/edit/<int:pk>/', views.ExperienceUpdateView.as_view(), name='experience_edit'),
    path('experience/create/', views.ExperienceCreateView.as_view(), name='experience_create'),
    path('experience/delete/<int:pk>/', views.ExperienceDeleteView.as_view(), name='experience_delete'),
    path('education/', views.EducationView.as_view(), name='education'),
    path('education/edit/<int:pk>/', views.EducationUpdateView.as_view(), name='education_edit'),
    path('education/create/', views.EducationCreateView.as_view(), name='education_create'),
    path('education/delete/<int:pk>/', views.EducationDeleteView.as_view(), name='education_delete'),
]
