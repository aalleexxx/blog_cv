from django.urls import path

from . import views

urlpatterns = [
    path('CV', views.home_page),
]
