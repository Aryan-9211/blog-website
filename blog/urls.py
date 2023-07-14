from django.contrib import admin
from django.urls import path
from blog import views
from . import views_api

urlpatterns = [
    path("", views.home, name="home"),
    # path("login", views.login, name="login"),
    path('login/', views_api.LoginView, name='login'),
    path('register', views.register, name="register")
] 