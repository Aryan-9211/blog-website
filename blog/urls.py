from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login_view"),
    path('register/', register, name="register_view"),
    path('add-blog/', add_blog, name="add_blog"), 
    path('blog-detail/<title>', blog_detail, name="blog_detail"),
    path('see-blog/', see_blog, name="see_blog"),
    path('blog-delete/<id>', blog_delete, name="blog_delete"),
    path('blog-update/<title>', blog_update, name="blog_update"),
    path('logout/', logout, name="logout"),
    
] 