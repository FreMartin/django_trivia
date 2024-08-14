
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('question.urls')),
    path('', include('register_sesions.urls')),
    path('', include('fetch_trivia.urls')),
]
