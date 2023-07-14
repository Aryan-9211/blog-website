from django.urls import path
from . import views_api

urlpatterns = [
    path('login/', views_api.LoginView, name='login'),
    path('register/', views_api.RegisterView, name='register'),
] 