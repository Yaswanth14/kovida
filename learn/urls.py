from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from learn import views

urlpatterns = [
    path('', views.home, name='home'),
    path('learn', views.learn, name='learn'),
    path('course/<str:slug>', views.course, name="course")
]