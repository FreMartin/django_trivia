from django.urls import path
from .views import fetch_and_store

urlpatterns = [
    path('store/', fetch_and_store, name='store'),
]
