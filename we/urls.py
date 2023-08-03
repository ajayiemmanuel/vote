from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path ('', views.index, name = "index"),
    path ('about/', views.about, name = "about"),
    path ('contact/', views.contact, name = "contact"),
    path ('career/', views.career, name = "career"),
    path ('about/', views.about, name = "about"),
    path ('facebook/', views.facebook, name = "facebook"),
    path ('instagram/', views.instagram, name = "instagram"),



]