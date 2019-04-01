from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('appointment/', views.appointment, name="appointment"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),

]
