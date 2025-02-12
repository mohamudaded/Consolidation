from django.urls import path
from . import views
from .models import NewsArticle
from django.views.generic import ListView, DetailView
app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    # path('user_login/', views.user_login, name='user_login'),path('<int:pk>/', DetailView.as_view(model=NewsArticle, template_name="post.html", context_object_name='post')),  
    # path('<int:pk>/', DetailView.as_view(model=NewsArticle, template_name="post.html", context_object_name='post'), name='blog_detail'),  
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),  # post detail
]