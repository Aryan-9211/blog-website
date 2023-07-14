from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path('register/', views.register, name="register"),
    path('add-blog/', views.add_blog, name="add_blog"), 
    path('blog-detail/<title>', views.blog_detail, name="blog_detail"),
    path('see-blog/', views.see_blog, name="see_blog"),
] 