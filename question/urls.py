from django.urls import path

from .views import questions

urlpatterns = [
    path('trivia/', questions, name='trivia'),
]
