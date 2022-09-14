from django.contrib import admin
from django.urls import path, include
from hire import views

urlpatterns = [
    path('', views.hire, name='hire')
]