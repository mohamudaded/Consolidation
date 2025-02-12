from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),  # List all questions
    path('<int:question_id>/', views.detail, name='detail'),  # View a specific question
    path('vote/<int:question_id>/', views.vote, name='vote'),  # Vote on a question
    path('<int:question_id>/results/', views.results, name='results'),  # View results
]